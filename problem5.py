# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder. What is the smallest positive number
# that is evenly divisible by all of the numbers from 1 to 20?

all_factors = range(1,21)
i = 1

while True:
    mod_result = [i%x for x in all_factors]
    if sum(mod_result) == 0:
        print(i)
        break
    print(i)
    i += 1