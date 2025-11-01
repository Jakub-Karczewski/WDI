import math
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


def last_nonzero_in_fact(n, arr):
    if n <= 9:
        return arr[n]
    
    # https://math.stackexchange.com/questions/130352/last-non-zero-digit-of-a-factorial
    # this task is just impossible, but we will use that formula here xddd

    res = (last_nonzero_in_fact(n//5, arr) * arr[n % 10]) % 10

    if ((n % 100)//10) % 2 == 1:
        res = (4 * res) % 10
    else:
        res = (6 * res) % 10
    return res


D = [1 for _ in range(10)] # in order for D[0] to have value 1, because we will use it in multiplication
res = 1
for nr in range(1, 10, 1):
    res *= nr
    D[nr] = get_last_nonzero_digit(res)
print("Computed from 1-9:", D)


for i in [10, 27, 100, 200]:
    fact = calc_factorial(i)
    last_digit = get_last_nonzero_digit(fact)
    computed_last_digit = last_nonzero_in_fact(i, D)
    assert last_digit == computed_last_digit, f"mismatch for {i}! : expected {last_digit}, got {computed_last_digit}"
