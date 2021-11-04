# Problem Set 8

## Overview

This problem set explores three algorithms for solving 3-coloring:
- Exhaustive search
- Augmentation of 2-coloring algorithm with independent sets (covered in Active Learning)
- Reduction to SAT

We have implemented exhaustive search for you as a benchmark. You will implement the augmentation of the 2-coloring algorithm in parts 1a and 1b, and the reduction to SAT in 1c. In 1d, you will compare the performance of these three algorithms.

*Make sure to pull from the course source often or check Ed for updates. We hope to release a perfect problem set but sometimes we add to the problem set to make things easier or fix obscure bugs.*

## Instructions

**Problem 1a**: First, implement the O(n+m)-time algorithm for 2-coloring that we covered in class, verifying its correctness by running `python3 -m ps8_tests 2`. You will need to adapt the given BFS pseudocode so that it works on all graphs, regardless of whether they are connected.

**Problem 1b**: Implement the O(1.89^n)-time algorithm for 3-coloring that you studied in Active Learning Exercise 5, also verifying its correctness by running `python3 -m ps8_tests 3`.

**Problem 1c**: Finally, implement the reduction from 3-coloring to SAT given in class,  producing an input that can be fed into the SAT Solver Glucose, and verify its correctness by running `python3 -m ps8_tests 3`.

**Problem 1d**: Compare the performance of the three 3-coloring algorithms on different types of graphs. We have provided most of experiment code in `ps8_experiments.py`; all you have to do is try different parameters and analyze the results.

**Conclusion**: If your work passes the local tests, includes the figure for your generated chart, and answers 1b, you should be in good shape to get full marks for this problem.
You can check that you pass all tests by running `python3 -m ps8_tests`.

## Running the Code

The problem set includes some starter code in `ps8.py`. To run the code, type in your terminal:

```bash
python3 -m ps8
```

## Running the Included Tests

The problem set also includes some tests for you to test your code.

To run the tests, type in your terminal:

```bash
python3 -m ps8_tests 2
```

```bash
python3 -m ps8_tests 3
```

```bash
python3 -m ps8_experiments
```