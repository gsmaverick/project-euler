# Problem 4:
#   A palindromic number reads the same both ways. The largest palindrome made from the product of two
#   2-digit numbers is 9009 = 91 99.
#   Find the largest palindrome made from the product of two 3-digit numbers.

import utils

highest = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        if utils.is_palindrome(str(i * j)) and (i * j) > highest:
            highest = i * j

print(highest)
