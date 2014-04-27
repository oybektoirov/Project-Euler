# -*- coding: utf-8 -*-
"""
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum.
Answer: 25164150
"""

def sqSumEach(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i ** 2  
    return sum
    
def sqSumAll(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return sum ** 2

def difference(a, b):
    return a - b
    
print difference(sqSumAll(100), sqSumEach(100))