# The prime factors of 13195 are 5, 7, 13, and 29. What is the largest prime
# factor of the number 600851475143?

import math

target = 600851475143
#target = 13195
#target = 10
        
def find_all_factors(target):
    factors = []
    for x in range(1, target+1):
        if target%x == 0:
            factors.append(x)
            print(factors)
            if target/x in factors:
                break
    print('')
    print(factors)
    print('')
    for x in reversed(factors[0:-2]):
        factors.append(int(target/x))
    return factors
                
def remove_composite_numbers(factors):
    primes_only = []
    for x in factors[1:-1]:
        for y in range(2,x):
            if x%y == 0:
                break
        if y == x-1:
            primes_only.append(x)
    return primes_only
        
    
all_factors = find_all_factors(target)
print(*all_factors)

print(*remove_composite_numbers(all_factors))