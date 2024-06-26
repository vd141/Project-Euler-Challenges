# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get, 3, 6, and 9. The sum of these multiples is 23. Find the sum of all multiples of 3 or 5 below 1000.

multiples_of_3 = set(range(3,1000,3))
multiples_of_5 = set(range(5,1000,5))

sum_of_all_multiples = sum(multiples_of_3.union(multiples_of_5))

print(sum_of_all_multiples)