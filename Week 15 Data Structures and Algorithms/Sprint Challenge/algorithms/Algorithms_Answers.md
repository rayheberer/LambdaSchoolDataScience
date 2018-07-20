Add your answers to the Algorithms exercises here.

__Exercise I__

a) Each iteration of the loop will add a factor of _n^2_ to a, until a equals _n^3_. There are _n_ factors of _n^2_ in _n^3_, so the runtime complexity is _O(n)_.

b) In the worst case where none of the elements of the array checked are greater than the target, there will be as many loops as there are times one can half a number before it becomes less than 1 (assuming the array is 1-indexed to avoid an infinite loop). This is just the base 2 logarithm of that number, which in this problem is the length of the array. The runtime complexity is then _O(log(n))_.

c) On each iteration of the outer loop, the two inner loops each execute 8 times, or 64 times in total, taking a constant amount of time for any _n_. The outer loop runs a factor of _sqrt(n)_ times, making the overall runtime complexity _O(sqrt(n))_.

d) The inner loop will run _n_ times, while the outer will run _log(n)_ times, making the overall runtime complexity _O(nlog(n))_.

e) The very inner loop will always run 10 times, while for large _n_, all 3 outermost loops will run _n_ times. The runtime complexity is _O(n^3)_.

f) `bunnyEars` will recurse once for every value between _n_ and 0, making it _O(n)_.

g) Indexing into an array in a language like C++ can be done in constant time. In the worst case, none of the elements in the array equal the target, which means `search` will be called for every size between _n_ and 0, making the function _O(n)_.

__Exercise II__

a) The max difference can be found by finding the maximum value in the array, and the minimum value in the array. This could be done with one pass through the array.

```
def max_difference(arr):
    maximum = -float('inf')
    minimum = float('inf')

    for element in arr:
        if element > maximum:
            maximum = element
        if element < minimum:
            minimum = element

    return maximum - minimum
```

b) If we initialize an adjustment value of 0.25 * _n_, initially throw an egg off the middle floor, and at each step multiply it by another factor of one half, then we can create a strategy that finds the appropriate _f_ in _O(log(n))_.

```
def find_f(n):
    adjustment = n // 4
    f = n // 2

    while adjustment > 1:
        result = throw_egg(f)

        if result == 'broken':
            f = f - adjustment
        else:
            f = f + adjustment

        adjustment = adjustment // 2

    f = narrow_in_on_result(f)
    return f
```

In the pseudocode, there may be some additional single-step wiggling done at the end to confirm that we have the correct floor, captured in `narrow_in_on_result`, but this will run in constant time, not affecting the runtime complexity of the overal strategy.

__Exercise III__

a) If the pivot is the first element of the array, then in the sorted case, every other element will be added to the `greater` array. So `quicksort` will be called a number of times equivalent to the length of the array (_n_). Each time it will make _O(n)_ comparisons, giving the algorithm a runtime complexity of _O(n^2)_ in this case.

b) In this case `quicksort` will recurse _O(log(n))_ times. Each call makes _O(n)_ comparisons, giving the algorithm a runtime complexity of _O(nlog(n))_.