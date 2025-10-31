import math
def calc_factorial(num): # function to calculate factorial of a number, can be used for small numbers only
    assert num >= 0, "we cannot calculate factorial of < 0 number"

    fact = 1
    for i in range(1, num+1, 1):
        fact *= i
    return fact

def get_last_nonzero_digit(N):
    if N == 0:
        assert False, "number cannot be 0"

    while True:
        # we stop counting when we reach a non-zero digit, because our number is not zero we will reach it eventually
        if N % 10 != 0: 
            return N % 10
        
        N = N//10 # Removing current last digit, going to the 'left' digit in number


def get_length_of_number(n):
    return math.floor(math.log10(n)) + 1

def last_nonzero_digit_in_factorial(n):
    # first thing we can observe is that trailing zeros do not affect the last non-zero digit
    # Also, we still multiply the repeating sequence of last non-zero digits from 1 to 10 of numbers in factorial
    
    # Unfortunately, this sequence is affected by the number of 2s and 5s we have in our factorial
    # because they create trailing zeros when paired together, and it will "shift" our sequence
    # Additionally, we can observe that for every n! number of 2 factors is greater than or equal number of 5 factors
    # It can be proven using the formula for calculating factors of a prime p (in our case 2 and 5)
    # in n!, this formula is used in the "zeros_at_the_end.py" file

    # Also, we can note that, for example for numbers lesser than 5^3 = 125,
    # we will create at most 3 trailing zeros in one step (one step is multiplying by next number in factorial),
    # because we can have at most 3 new factors of 5
    # This way, we need to store only log5(n) last non-zero digits for n factorial

    last_digit = 1
    factors_of_5 = 0
    factors_of_2 = 0

    powers_of_5 = []
    powers_of_2 = []
    
    current_power = 5
    while True:
        powers_of_5.append(current_power)
        if current_power * 5 > n:
            break
        current_power *= 5

    current_power = 2
    while True:
        powers_of_2.append(current_power)
        if current_power * 2 > n:
            break
        current_power *= 2

    # needed_length = 2 # how many last nonzero digits we need to store currently (it will change with every new power of 5)
    # current_max_power_of_5 = 25 # we increase needed_length when we reach 25, 125, 625, ...

    for i in range(1, n+1):
        if i % 2 == 0 or i % 5 == 0:
            ind1 = 0

            # if our number is a multiply of 2 ^ k it is divisible by all lower powers of 2 as well
            while len(powers_of_2) > 0 and i % powers_of_2[ind1] == 0:
                factors_of_2 += 1
                ind1 += 1

            # same for 5s
            ind2 = 0
            while len(powers_of_5) > 0 and i % powers_of_5[0] == 0:
                factors_of_5 += 1
                ind2 += 1

            # we remove equal number of 2s and 5s to avoid creating trailing zeros
            min_ind = min(ind1, ind2)

            if ind2 > min_ind:
                # case when we have more 5s than 2s, we need to remove extra 5s
                last_digits  = (last_digits % 10 * (((i // 10**min_ind) // 5**(ind2-ind1) ) % 10)) % 10
            else:
                last_digits *= (i // 10**min_ind)

            # if i == current_max_power_of_5:
            #     needed_length += 1
            #     current_max_power_of_5 *= 5

            assert factors_of_2 >= factors_of_5, "checking our assumption that number of 2s >= number of 5s"
        else:
            last_digits  = (last_digits % 10 * (i % 10)) % 10

