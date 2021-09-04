from ps0 import BinaryTree,calculate_size,FindSubtree


# Generated a full/balanced binary tree of `height`
def gen_tree(height, counter = {"val": 1}):
    # Counter needs to be an obj to pass ref
    # Counter needs to be a param if modified or it will be local
    def create_tree_node(counter=counter):
        # T = ps0.BinaryTree(counter["val"])
        T = BinaryTree(counter["val"])
        # increment counter for key
        counter["val"] += 1
        return T
    def gen_tree_inner(height):
        if height == 1:
            return create_tree_node()
        else:
            T = create_tree_node()
            T.left = gen_tree(height - 1)
            T.right = gen_tree(height - 1)
            return T
    return gen_tree_inner(height)

# Removes the outmost branch at `depth` and `side`
def remove_branch(T, depth = 1, side="left"):
    if depth == 1:
        setattr(T, side, None)
    else:
        remove_branch(getattr(T, side), depth - 1, side)
    return T

# Performs a singel check in O(n) time so it CANNOT be used in a search to create a O(n) Find Alg
def check_subtree(T,L,U):
    q = [T]
    index = 0
    while True:
        if index >= len(q):
            break
        current = q[index]
        index += 1
        if current.left: q.append(current.left)
        if current.right: q.append(current.right)
    size = len(q)
    return L <= size <= U
def check_if_in_subtree(T,key):
    q = [T]
    index = 0
    while True:
        if index >= len(q):
            break
        current = q[index]
        index += 1
        if current.left: q.append(current.left)
        if current.right: q.append(current.right)
    keys = [n.key for n in q]
    return key in keys
    

def test():
    tests = [
        # Format: (input, postprocessing, expected result)

        # Basic Tests
        (gen_tree(1), (lambda T: T), 1),
        (gen_tree(2), (lambda T: T), 3),
        (gen_tree(3), (lambda T: T), 7),
        (gen_tree(8), (lambda T: T), 255),
        (gen_tree(3).left, (lambda T: T), 3),
        (gen_tree(3).left.right, (lambda T: T), 1),
        (gen_tree(3).right, (lambda T: T), 3),
        # Test nodes/subtree
        (gen_tree(3), (lambda T: T.left), 3),
        (gen_tree(3), (lambda T: T.right), 3),
        (gen_tree(3), (lambda T: T.right.left), 1),
        (gen_tree(2), (lambda T: T.left), 1),
        # Tests unbalanced tree
        (remove_branch(gen_tree(2), 1), (lambda T: T), 2),
        (remove_branch(gen_tree(3), 1), (lambda T: T), 4),
        (remove_branch(gen_tree(8), 1), (lambda T: T), 255 - 127),
    ]
    print("Problem 1 Tests:")
    for i,test in enumerate(tests):
        calculate_size(test[0])
        res = test[1](test[0])
        score = res and hasattr(res, "temp") and res.temp == test[2]
        print("Test " + str(i + 1) + ": ", "Passed" if score else "Failed")
    
    tests_3 = [
        # Format: (input, postprocessing, expected result)

        # Basic Tests
        (gen_tree(3), (1,2)),
        (gen_tree(4), (1,3)),
        (gen_tree(3), (1,3)),
        (gen_tree(3), (1,6)),
        # Tests unbalanced tree
        (remove_branch(gen_tree(2), 1), (0,1)),
        (remove_branch(gen_tree(3), 1), (1,2)),
        (remove_branch(gen_tree(8), 1), (48,100)),
        (remove_branch(gen_tree(8), 1), (3,21)),
    ]
    print()
    print("Problem 3 Tests:")
    for i,test in enumerate(tests_3):
        T = test[0]
        res = FindSubtree(T, test[1][0], test[1][1])
        key = res.key if res else None
        # Check L,U
        score = res and check_subtree(res, test[1][0], test[1][1])
        # Check parent pointer
        score = score and not check_if_in_subtree(T, key)
        print("Test " + str(i + 1) + ": ", "Passed" if score else "Failed")

if __name__ == "__main__":
    test()