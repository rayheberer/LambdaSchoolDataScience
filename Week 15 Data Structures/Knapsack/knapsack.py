#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def brute_knapsack_solver(items, capacity):
    # base case
    if capacity == 0:
        return 0, 0, []
    
    max_value = 0
    size = 0
    knapsack = []
    for item in items:
        # only consider items that are below the current capacity
        if item.size > capacity:
            continue

        remaining_capacity = capacity - item.size
        remaining_items = items.copy()
        remaining_items.remove(item)
        
        value, _, subsack = brute_knapsack_solver(remaining_items, remaining_capacity)
        value += item.value
        subsack.append(item.index)

        if value > max_value:
            max_value = value
            knapsack = subsack
    
    size = sum([items[item-1].size for item in knapsack])
    return max_value, size, knapsack

def iterative_knapsack_solver(items, capacity):
    cache = {}
    knapsack = {}
    for weight in range(0, capacity+1):
        cache[0, weight] = 0
        knapsack[0, weight] = []

    for index in range(1, len(items)+1):
        for weight in range(0, capacity+1):
            if items[index-1].size > weight:
                cache[index, weight] = cache[index-1, weight]
                knapsack[index, weight] = knapsack[index-1, weight]
            else:
                with_new = cache[index-1, weight-items[index-1].size] + items[index-1].value
                without_new = cache[index-1, weight]
                
                if with_new > without_new:
                    cache[index, weight] = with_new
                    knapsack[index, weight] = knapsack[index-1, weight-items[index-1].size] + [index]
                else:
                    cache[index, weight] = without_new
                    knapsack[index, weight] = knapsack[index-1, weight]


    value = cache[len(items), capacity]
    knapsack = knapsack[len(items), capacity]
    size = sum([items[item-1].size for item in knapsack])
    return value, size, knapsack

def greedy_knapsack_solver(items, capacity):
    weighted_items = sorted([item for item in items], 
                            key=lambda item: item.value/item.size,
                            reverse=True)
    knapsack = []
    size = 0
    value = 0

    while size + weighted_items[0].size <= capacity:
        item = weighted_items.pop(0)
        knapsack.append(item.index)
        size += item.size
        value += item.value

    return value, size, knapsack

def knapsack_solver(items, capacity, strategy):
    if strategy == 'brute':
        print('Brute force')
        algorithm = brute_knapsack_solver
    elif strategy == 'iterative':
        print('Iterative bottom-up')
        algorithm = iterative_knapsack_solver
    elif strategy == 'greedy':
        print('Greedy')
        algorithm = greedy_knapsack_solver
    else:
        return 'strategy must be one of {"brute", "iterative", "greedy"}'

    value, size, knapsack = algorithm(items, capacity)
    knapsack = map(str, knapsack)
    return 'Value: {}\nSize: {}\nChosen: {}\n'.format(value, size, ','.join(knapsack))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []
        
        if len(sys.argv) > 3:
            strategy = sys.argv[3].strip()
        else:
            strategy = 'iterative'

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
        file_contents.close()
        print(knapsack_solver(items, capacity, strategy))
    else:
        print('Usage: knapsack.py [filename] [capacity]')