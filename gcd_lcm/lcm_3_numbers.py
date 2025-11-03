import random
def prime_factorization(N:int)->list[int]:
    prime_factors = []
    if N <= 1:
        return []
    for f in [2, 3, 5]: 
        nr = 0
        while N % f == 0:
            N //= f
            nr += 1
        if nr > 0:
            prime_factors.append([f, nr])

    i = 6
    while i*i <= N:
        for f in [i+1, i+5]:
            nr = 0
            while N % f == 0:
                N //= f
                nr += 1
            if nr > 0:
                prime_factors.append([f, nr])
        i += 6

    if N > 1:
        prime_factors.append([N, 1])
    return prime_factors

def calc_factorized_number(factors):
    num = 1
    for k, p in factors:
        num *= k**p
    return num

def lcm_naive(numbers):
    assert len(numbers) > 0
    mult = 1
    max_number = numbers[0]
    for x in numbers:
        mult *= x
        max_number = max(max_number, x)

    for l in range(max_number, mult+1, 1):
        flag = True
        for x in numbers:
            if l % x != 0: # not divisible
                flag = False
                break
        if flag:
            return l


def lcm(numbers):
    n = len(numbers)
    factorized = [prime_factorization(x) for x in numbers] # This array will be 3D, because function returns array m x 2
    # every factorized[i] is sorted, because we add prime factors increasingly
    indexes = [0 for _ in range(n)]

    lcm_factorized = []
    print(factorized)

    while True:
        found = False # this flag will be False if all the elements have been merged
        curr_min_factor = float('inf')
        max_factor_power = 0

        for i in range(n):
            curr_idx = indexes[i]

            if curr_idx < len(factorized[i]): # if we have elements left in array of factors
                curr_factor, curr_power = factorized[i][curr_idx][0], factorized[i][curr_idx][1]
                curr_min_factor = min(curr_min_factor, curr_factor)
                found = True

        if not found:
            break
                
        for i in range(n):
            curr_idx = indexes[i]
            if curr_idx < len(factorized[i]):
                curr_factor, curr_power = factorized[i][curr_idx][0], factorized[i][curr_idx][1]
                if curr_factor == curr_min_factor: # If we found equal we take the maximum of powers
                    indexes[i] += 1 # we move the index, because this factor was already computed
                    max_factor_power = max(max_factor_power, curr_power)

        lcm_factorized.append([curr_min_factor, max_factor_power])

    return calc_factorized_number(lcm_factorized)


for i in range(10):
    T= [random.randint(2, 100) for _ in range(3)]
    print(T)
    print(lcm(T) == lcm_naive(T))
    print()

