# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder. What is the smallest positive number
# that is evenly divisible by all of the numbers from 1 to 20?

all_factors = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
i = 2520

while True:
    mod_result = [i%x for x in all_factors]
    if sum(mod_result) == 0:
        print(i)
        break
    print(i)
    i += 2520

    # got 232792560 by incrementing by 2520