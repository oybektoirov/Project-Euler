def n_prime(limit):
    num = 7
    prime_list = [2, 3, 5]
    while True:
        if is_prime(num, prime_list):
            prime_list.append(num)
            if len(prime_list) == limit:
                return prime_list[-1]
        num += 2
            
def is_prime(num, prime_list):
    for i in prime_list:
        if num % i == 0: return False
    return True
    
print n_prime(10001)
    
      