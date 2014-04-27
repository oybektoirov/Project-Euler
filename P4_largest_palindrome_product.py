# -*- coding: utf-8 -*-
"""
A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91 × 99.
Assignment: Find the largest palindrome made 
from the product of two 3-digit numbers.
Answer: 906609
"""
def largestPalindrome():
    top = 1099
    largestPalindrome = 0
    for first in range(100, 1000):
        first = top - first
        for second in range(100, 1000):
            second = top - second
            product = first * second
            if product < largestPalindrome: 
                break
            else:
                # checking for palindrome
                for i in range(len(str(product))):
                    if str(product)[i] != str(product)[-(i + 1)]:
                        break
                    if i + 1 == len(str(product)):
                        largestPalindrome = product
    return largestPalindrome

print largestPalindrome()
            
            
