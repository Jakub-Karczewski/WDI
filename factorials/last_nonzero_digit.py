def calc_factorial(num): # function to calculate factorial of a number, can be used for small numbers only
    fact = 1
    for i in range(1, num+1, 1):
        fact *= i
    return fact


def get_last_nonzero_digit(N):
    assert N != 0, "number cannot be 0"
    while True:
        # we stop counting when we reach a non-zero digit, because our number is not zero we will reach it eventually
        if N % 10 != 0: 
            return N % 10
        
        N = N//10 # Removing current last digit, going to the 'left' digit in number


def get_last_digit_of_power(base, k):
    if base in [1, 5, 6]:
        return base
    
    first, act = base, (base * base) % 10
    cycle = [base]
    while act != first:
        cycle.append(act)
        act = (act * base) % 10
    idx = ((k % len(cycle)) - 1) % (len(cycle)) # because we index from 0, % len(cycle) ensures that we cycle over the list of values
                                                # e. g -1 mod 4 == 3 mod 4, and we will go to the other end
    return cycle[idx]


def last_nonzero_in_fact(n, arr):
    if n <= 9:
        # for small n's we have already calculated values, this are our ending points in recursion
        return arr[n]
    
    # https://math.stackexchange.com/questions/130352/last-non-zero-digit-of-a-factorial
    # that is the proof for the formula, this proof is not possible to understand without some math background

    # Probably this can be understood more easily with intuition presented in:
    # https://youtu.be/RmENut3ZmnM

    # Let's look at 25!
    # first we can extract all 5's, thus we have:
    # 5^5 * 5! * (1 * 2 * 3 * 4) * (6 * 7 * 8 * 9) * (11 * 12 * 13 * 14) * ...
    # From the video above we know that each of the parenthesis can be reduced into
    # 6 (mod 10) * 4 (mod 10)
    # 1 * 2 * 3 * 4 = 6 * 4
    # 6 * 7 * 8 * 9 = 6 * (7 * 8 * 9) = 6 * (6 * 9) = 6 * 4
    # 11 * 12 * 13 * 14 = (11 * 12 * 13) * 14 = (6 * 4)
    # 16 * 17 * 18 * 19 = 6 * (7 * 8 * 9) = 6 * 4, same as case 2 lines above
    # 21 * 22 * 23 * 24 = (1 * 2 * 3) * 4 = 6 * 4
    # also we can see that, despite the fact 25 is divisible by 5^2
    # it will still not break our solution, that relies on removing only 1 factor of 5 from a number
    # Because this second 5 will be used in calculating 5! that came from extracting 5 * 10 * 15 * 20 * 25
    # Even if we would have 125!, after extracting multiplies of 5, we would get 25! * (5^(25))
    # And the lower powers of 5 would be included in next recursion

    # So, if we return to 25! :
    # we get (5^5 * 5!) * (4 * 6)^5 = 5^5 * 5! * 4^5 = (2^5 * 5^5) * 2^5 * 5! = 2^5 * 5!
    # Also, we need to think about the case when a number is not divisible by 5, like 27
    # we get: (answer for 25) * (26 * 27) = (answer for 25) * (27 % 5)!

    # Let's explain that: 
    # 1 = 6 in our case, because 1 does not change remainder, and also 6 multiplied by any even number also does not
    # (6 * 7) = 2 = (1 * 2)
    # (6 * 7 * 8) = 6 = (1 * 2 * 3)
    # (6 * 7 * 8 * 9) = ((6 * 8) * (7 * 9)) = (8 * 3) = 4 = (4 * 6) = (1 * 2 * 3 * 4)
    # this way, we can treat remainder from e.g 23 same as remainder for 28

    # if we introduce variable n and say, that D(n) is the last nonzero digit of n!, we get:
    # n! = 5^(n//5) * (n//5)! * (4 * 6)^(n//5) * (n % 5)!
    # Thus:
    # D(n) = (5^(n//5) * 2^(n//5)) * D(n//5) * 2^(n//5) * D(n%5) = D(n//5) * 2^(n//5) * D(n%5)
    # We can see that the only difficult to calculate factor is D(n//5)
    # the last digit of 2^k can be computed instantly, because it is a cycle 2, 4, 8, 6
    # also D(n%5) can be easily calculated, because it is at most 4!
    # so for each iteration we recursively only call D(n//5)
    # This gives up logarithmic complexity and enables us to calculate easily answer for (10^100)!

    return (last_nonzero_in_fact(n//5, D) * D[n % 5] * get_last_digit_of_power(2, n//5)) % 10


D = [1 for _ in range(10)] # in order for D[0] to have value 1, because we will use it in multiplication
res = 1
for nr in range(1, 10, 1):
    res *= nr
    D[nr] = get_last_nonzero_digit(res)


print("Computed from 1-9:", D)
print()


for i in [10, 27, 100, 200]:
    fact = calc_factorial(i)
    last_digit = get_last_nonzero_digit(fact)
    computed_last_digit = last_nonzero_in_fact(i, D)

    print(last_digit == computed_last_digit)
    assert last_digit == computed_last_digit, f"mismatch for {i}! : expected {last_digit}, got {computed_last_digit}"

for k, p in [(2, 50), (3, 20), (4, 17), (7, 34), (9, 15)]:
    last_digit = get_last_nonzero_digit(k ** p)
    computed_last_digit = get_last_digit_of_power(k, p)
    print(last_digit == computed_last_digit)
    assert last_digit == computed_last_digit, f"mismatch for {k}^{p} : expected {last_digit}, got {computed_last_digit}"