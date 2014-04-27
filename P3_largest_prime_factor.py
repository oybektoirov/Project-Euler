"""
The prime factors of 13195 are 5, 7, 13 and 29.
Assignment: Find the largest prime factor of the number 600851475143.
Answer: 6857
"""

def findPrime():
    pList = []
    num = 600851475143
    original = 600851475143
    total = 1
    for prime in range(1, 1000000, 2):
        if num % prime == 0:
            pList.append(prime)
            for n in pList: total *= n
            if total == original: return pList[-1]
            num /= prime
            total = 1
            
print findPrime()
    
        