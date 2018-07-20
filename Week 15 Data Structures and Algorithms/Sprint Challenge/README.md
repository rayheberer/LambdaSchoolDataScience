# Sprint Challenge: Data Structures and Algorithms

For the data structures portion of this sprint challenge, you'll be implementing a few functions that build off of some of the data structures you implemented in the first half of the week. Then you'll be analyzing the runtimes of these functions.

For the algorithms portion of the sprint challenge, you'll be answering the questions posed in the `exercises.pdf` file regarding runtime complexities and algorithmic paradigms.

## Data Structures

### Task 1. Implement Depth-First and Breadth-First Traversal on the Binary Search Tree Class 
Navigate into the `ex_1` directory in the `data_structures` directory. Inside, you'll see the `binary-search-tree.py` file with a complete implementation of the binary search tree class. Your first task is to implement the methods `depth_first_for_each` and `breadth_first_for_each` on the `BinarySearchTree` class:

   * `depth_first_for_each(cb)` receives a callback function as a parameter. This method iterates over the binary search tree in [depth-first](https://en.wikipedia.org/wiki/Depth-first_search) order, applying the supplied callback function to each tree element in turn. 
   * `breadth_first_for_each(cb)` receives a callback function as a parameter. This method iterates over the binary search tree in [breadth-first](https://en.wikipedia.org/wiki/Breadth-first_search) order, applying the supplied callback function to each tree element in turn.

NOTE: In Python, anonymous functions are referred to as "lambda functions". When passing in a callback function as input to either `depth_first_for_each` or `breadth_first_for_each`, you'll want to define the callbacks as lambda functions. For more information on lambda functions, check out this documentation: [https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)

Run `python3 test_binary_search_tree.py` to run the tests for these methods to ensure that your implementation is correct.

### Task 2. Implement Heapsort
Inside the `ex_2` directory you'll find the `heap.py` file with a working implementation of the heap class. Your second task is to implement a sorting method called [heapsort](https://en.wikipedia.org/wiki/Heapsort) that uses the heap data structure in order to sort an array of numbers. Your `heapsort` function should return a new array containing all of the sorted data.

Run `python3 test_heap.py` to run the tests for your `heapsort` function to ensure that your implementation is correct.

### Task 3. Analyze some runtimes
Open up the `Data_Structures_Answers.md` file. This is where you'll jot down your answers for the runtimes of the functions you just implemented. Be sure to also answer any other questions posed in the `Answers.md` file!

## Algorithms
For the algorithms portion of the sprint challenge, you'll be answering questions posed in the `exercises.pdf` document inside the `algorithms` directory. Add your answers to the questions in the `Algorithms_Answers.md` file.