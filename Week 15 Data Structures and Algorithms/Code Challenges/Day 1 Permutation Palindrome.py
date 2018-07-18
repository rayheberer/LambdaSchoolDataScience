"""
Write a function that, given a string, determines whether any permutation of that string is a palindrome. 

Examples:

"civic" should return True
"ivicc" should return True
"civil" should return False
"livci" should return False

Yes, yes, "ivicc" itself is not a palindrome, but it can be rearranged into a valid palindrome, i.e. "icvci", which is a valid palindrome. 
"""

from collections import Counter

def is_permutation_palindrome(string):
    counts = Counter(string)
    
    odds = 0
    for count in counts.values():
        if count % 2 != 0:
            odds += 1
            if odds > 1:
                return False
    return True