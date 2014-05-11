def summation_of_primes():
    prime_list = [2, 3, 5]
    summation = 10
    for i in range(7, 2000000, 2):
        if isPrime(i, prime_list):
            prime_list.append(i)
            summation += prime_list[-1]
    return summation
    
def isPrime(num, prime_list):
    for i in prime_list:
        if num % i == 0: return False
    return True
        
print summation_of_primes()