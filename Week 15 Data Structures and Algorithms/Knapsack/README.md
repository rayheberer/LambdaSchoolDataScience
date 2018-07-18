# Algorithmic Paradigms

When it comes to solving problems, there are _many_ ways to go about doing it. Frankly, the number of ways any one problem can be solved are limited only by your creativity and imagination.

![Alt Text](https://media.giphy.com/media/QFsPtlrcMlS8w/giphy.gif)

That being said, there are a few approaches for certain classes of problems that have stood the test of time, due to their efficiency and effectiveness. Imagination and creativity and both all well and good when you encounter a new problem, but at the same time we don't want to also constantly be re-inventing the wheel. 

For this sprint, we'll be exploring a few of these battle-tested algorithmic paradigms and applying them to a few problems. The main problem we'll be looking at is colloquially named "The Knapsack Problem".

## "The Knapsack Problem"

The Knapsack problem can be summarized like so:

Suppose you are Indiana Jones, and you have found the secret entrance to the Temple of Doom. Before you is a multitude of artifacts and treasures - pots, gemstones, works of art, and more. These belong in a museum! But there are soldiers hot on your heels, and you can only carry so much...

You, brave explorer, are facing the knapsack problem - maximizing the value of a set of items you select that are constrained by total size/weight. The size and the value of an item need not be correlated - the most precious item may be a tiny gemstone. But it turns out it's pretty tricky to get a truly optimal solution, and that a bruteforce approach really doesn't scale.

A bit more motivation - this is a very general optimization problem that can be applied in a multitude of situations, from resource selection and allocation to stuffing stolen goods in knapsacks.

![xkcd "NP-Complete"](https://imgs.xkcd.com/comics/np_complete.png "General solutions get you a 50% tip.")

## Objectives

The main objectives for this sprint are to:

* Try to solve a hard algorithmic problem
* Try a variety of algorithmic approaches
* Learn about performance/benchmarking, play with some actual data

## Getting Started

The specific goal of this exercise is to write a program that takes input files that look like this:

```
1 42 81
2 42 42
3 68 56
4 68 25
5 77 14
6 57 63
7 17 75
8 19 41
9 94 19
10 34 12
```

The first row number is just a row/observation number, to facilitate reading and referring to items. The second number is the size/cost of the item, i.e. the cost of putting it in your knapsack. The third number is the value, i.e. the utility/payoff you get for selecting that item. The program should also take as input a total size, which can just be a number passed from the command line. So execution may look like this: `python knapsack.py input.txt 100`.

The goal is to select a subset of the items to maximize the payoff such that the cost is below some threshold. That is, the output should be a set of items (identified by number) that solves the Knapsack problem. It's also worth outputting the total cost and value of these items. This can all just be printed and may look something like below.

This is *not* a solution, just an example:

```
Items to select: 2, 8, 10
Total cost: 98
Total value: 117
```

### Task 1: Implement a Brute Force Naive Solution

For first steps, just think a bit about how you might naively solve this with brute force. The above data is small enough that such a solution should work, so give it a go. More to come soon - larger problems that will require more sophisticated approaches.

### Task 2: Implement a Better Solution

More specifically, try to use one (or more) of the algorithmic paradigms that were discussed in lecture, namely, memoization or bottom-up iterative, in order to come up with a better solution that can handle larger inputs than what your brute force solution can handle.

Another line of thinking you may wish to try is to come up with a heuristic, or a mental shortcut, that can be used to solve this particular problem. For example, what if we tried to rank each possible item by their value/weight ratio? :wink:

### Stretch Goals

If you've implemented a working solution to the knapsack problem using one of the paradigms we discussed in lecture, try implementing another solution using a different paradigm!

---

The `answers.txt` file includes the expected answers for each of the data files. Note that all the runs use a capacity of 100. 

The `knapsack-generator.js` file is a utility that allows you to generate larger data sets, so you can test your implementation more thoroughly. 
