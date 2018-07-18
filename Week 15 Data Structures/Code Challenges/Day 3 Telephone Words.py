"""
It's Telephone Words again!

Write a function that takes a string of digits up to a length of four. The function should return a list of all of the possible letter combinations that can be written using those digits.

Example:

telephone_words('2745')
    # returns ['APGJ',
               'APGK',
               ...,
               'CSIL']

Note that digits 0 and 1 don't have letters associated with them in the digits_to_letters object. They should be left as numbers.
"""

from itertools import product

digits_to_letters = {
    0: '0',
    1: '1',
    2: 'ABC',
    3: 'DEF',
    4: 'GHI',
    5: 'JKL',
    6: 'MNO',
    7: 'PQRS',
    8: 'TUV',
    9: 'WXYZ'
}

def telephone_words(digits):
    letters = [list(digits_to_letters[int(digit)]) for digit in digits]
    return [''.join(t) for t in product(*letters)]