# A palindromic number reads the same both ways. The largest palindrome made
# from the product of 2-digit numbers is 9009 = 91 x 99. 
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(word):
    word = str(word)
    if word == word[::-1]:
        return True
    return False

def return_factor_range_as_list():
    digits = int(input('How many digits is your factor? '))
    min_factor = 10**(digits-1)
    max_factor = ''
    for x in range(digits):
        max_factor += '9'
    print(*[min_factor, int(max_factor)])
    return [min_factor, int(max_factor)]

def find_largest_palindrome():
    factor_range = return_factor_range_as_list()
    palindromes = []
    for x in range(factor_range[-1],factor_range[0]-1,-1):
        for y in range(factor_range[-1], factor_range[0]-1,-1):
            if is_palindrome(x*y):
                palindromes.append(x*y)
    return max(palindromes)

print(find_largest_palindrome())
