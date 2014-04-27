"""
2520 is the smallest number that can be divided by 
each of the numbers from 1 to 10 without any remainder.
Find the smallest positive number that is evenly 
divisible by all of the numbers from 1 to 20.
Answer: 232792560
"""

def smallestMult(num):
    searching = True
    smallest = 2520
    while searching:
        smallest += 2
        for i in range(1, num + 1):
            if smallest % i != 0: break
            if i == num: searching = False
    return smallest
            
print smallestMult(20)
            
                