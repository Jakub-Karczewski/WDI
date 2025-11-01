def calc_factorial(num): # function to calculate factorial of a number, can be used for small numbers only
    fact = 1
    for i in range(1, num+1, 1):
        fact *= i
    return fact

def count_trailing_zeros(n): # function to count trailing zeros in a number
    nr = 0
    while True:
        if n == 0 or n % 10 > 0: # we stop counting when we reach a non-zero digit or our number becomes 0
            break
        nr += 1
        n //= 10
    return nr

def zeros_in_factorial(n): # function to count trailing zeros in n! using calculation of factors of 2 and 5
    num_twos, num_fives = 0, 0 # initialize counts of factors of 2 and 5
    two_pow, five_pow = 2, 5 # initialize powers of 2 and 5

    while two_pow <= n: # count until current power of 2 exceeds n
        num_twos += n//two_pow
        two_pow *= 2

    # for example, we have 10! = 1 * 2 ... * 10
    # multiples of 2 are 2, 4, 6 ...
    # first iteration: 10//(2^1) = 5, numbers: (2, 4, 6, 8, 10) - calculates all numbers
    # that are divisible by minimum 1st power of 2
    # second iteration: 10//(2^2) = 2, numbers: (4, 8) - calculates all numbers
    # that are divisible by minimum 2nd power of 2
    # third iteration: 10//(2^3) = 1, numbers: (8) - calculates all numbers
    # that are divisible by minimum 3rd power of 2

    # This way, if we have a factor 2^k in our factorial, due to our solution
    # it will be counted k times, once for each power of 2 it is divisible by.
    # Also, we will not count anything extra and do not need to
    # use the inclusion-exclusion principle

    # We do the same for counting factors of 5
    while five_pow <= n:
        num_fives += n//five_pow
        five_pow *= 5

    # Finally, we return the minimum of the two counts, because every 2 must be paired with a 5
    # to form a trailing zero (10 = 2 * 5)
    return min(num_twos, num_fives)


for N in [10, 20, 50, 100, 200]:
    # validate our optimized function against the direct calculation for small N
    print(count_trailing_zeros(calc_factorial(N)) == zeros_in_factorial(N))
