# The prime factors of 13195 are 5, 7, 13, and 29. What is the largest prime
# factor of the number 600851475143?

import math

#target = 600851475143
target = 13195
#target = 10
        
def find_factors(target, primes_only = False):
    factors = []
    if not primes_only:
        for x in range(1, target+1):
            if target%x == 0:
                factors.append(x)
                print(factors)
                if target/x in factors:
                    break
        print('')
        print(factors)
        print('')
        for x in reversed(factors[1:-2]):
            factors.append(int(target/x))
        return factors
        
    else:
        for x in range(1, target+1):
            if target%x == 0:
                
    
def eliminate_factor_if_not_prime(factors):
    for x in factors:
        find_factors(x,True)
    
print(*find_factors(target))