Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?

`depth_first_for_each` explores each node once, and performs either an `append` or a `pop` operation on the `visited` collection, which is implemented as a python list. Each of these operations can be done in constant time, therefore the full method runs in linear time with respect to the size of the input, or _O(n)_. 

2. What is the space complexity of your `depth_first_for_each` function?

Given a fully populated tree of depth _d_, `depth_first_for_each` will store at most _d_ nodes in its `visited` collection. Since a binary tree of depth _d_ will have O(_2^d_) nodes (_2^(d+1) - 1_ to be precise), the spacial complexity of the function is then _O(log(n))_, where _n_ is the number of nodes in the tree, and _log_ is the base 2 logarithm.

3. What is the runtime complexity of your `breadth_first_for_each` method?

This method explores every node once, performing constant runtime operations on each step. It is therefore _O(n)_. However, it is worth noting that _n_ itself grows exponentially with the depth of the tree.

4. What is the space complexity of your `breadth_first_for_each` method?

Given a tree of depth _d_, `breadth_first_for_each` will store _2^(d-1)_ nodes at most. This makes the space requirements of the method roughly par with space requirements of the tree itself, giving the method a space complexity of _O(n)_. 

5. What is the runtime complexity of your `heapsort` function?

Given an array of length _n_, `heapsort` will run _n_ `insert` operations and _n_ `delete` operations. `insert` and `delete` call `_bubble_up` and `_sift_down` respectively at most _log(n)_ times, so in the worst case, `heapsort` is _O(nlog(n))_.

6. What is the space complexity of the `heapsort` function? Recall that your implementation should return a new array with the sorted data. What would be the space complexity if your function instead altered the input array?

THe space requirement of the function, as it creates a copy of the original array, is just a multiple of the space requirement of the array. In other words, the space complexity of `heapsort` is linear, _O(n)_. If it altered the input array, then the algorithm itself would only need a constant amount of additional space, regardless of the size of the array, making it _O(1)_.