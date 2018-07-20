import unittest
from random import randint
from heap import heapsort

def gen_random_input(length, max):
  input = []
  for i in range(length):
    input.append(randint(0, max))
  return input

def is_sorted(arr):
  for i in range(len(arr) - 1):
    if arr[i] > arr[i+1]:
      return False
  return True

class HeapTests(unittest.TestCase):
  def test_heap_sort_correctness(self):
    length = randint(100, 1000)
    input = gen_random_input(length, 1000)
    output = heapsort(input)

    self.assertEqual(len(output), length)
    self.assertTrue(is_sorted(output))

if __name__ == '__main__':
  unittest.main()