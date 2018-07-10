# Reinforcement Learning - Coding Challenge 2

This coding challenge covers some of the basic mathematical functions that
appear in reinforcement learning. Visit this article:
https://medium.freecodecamp.org/an-introduction-to-reinforcement-learning-4339519de419

Read up to the line  "To be simple, each reward will be discounted by `gamma` to
the exponent of the time step." Today we'll be implementing the equation
immediately above that. For simplicity we'll assume that each round has a fixed
reward `R` and that the only thing changing the utility is the discount.

Your task is to calculate the total lifetime reward for a given `R` and `gamma`.
You should clone this repository, open it up locally, and open the file
`reward.py`. You'll see an empty function called `reward(gamma, R)`. Right now
it's set to return -1.0. Change it so that it returns the correct answer.
**This is the only file you should edit!**

A resource to review summation notation:
http://www.columbia.edu/itc/sipa/math/summation.html

## Testing your solution

The correctness of your code will be tested with `unittest`, a testing library
built in to Python. You can run tests in this directory as follows:

`python test_reward.py --verbose`

Depending on your computer it may be `python3` instead. And also the `--verbose`
flag is optional, but helpfully expands the output.

This command will run the tests contained in `test_reward.py` - you do not
need to edit this file, but please do check it out to see how it works. Unit
tests usually test expected input/output of a short function (a "unit" - in this
case the function `reward()` you are writing).

This particular test file has one always passing test and four tests that will
pass once you successfully complete the `reward()` function. The always passing
test is for you to be sure you're running the test properly - even before
writing code you should see 1 success and 4 failures if you run the tests.

If you're curious about `unittest` you can read more here:
https://docs.python.org/3.6/library/unittest.html

With a few exceptions if you know enough mathematics, there is no good way for a
program to calculate the exact value of an infinite sum. Besides the inherent
trickiness of infinite sums, this is true because of the unavoidable
approximateness of floating point arithmetic. Because of this, the tests are
written such that your result has to be within 1/1000th of the answer.
