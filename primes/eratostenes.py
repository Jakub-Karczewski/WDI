
def eratostenes(N):
    is_prime_arr = [True for _ in range(N+1)]
    i = 2
    primes_arr = []

    # every number that is not prime will have a factor less or equal than sqrt(N)
    # for example we take:
    # 15 = 5 * 3, where 3 < sqrt(15)
    # 35 = 7 * 5, where 5 < sqrt(35)
    # we can use that intuition, that the bigger 1st factor is the less the 2nd will be
    # and they will be equal, only if N is a square of a prime number e.g: 4, 9, 25, 49
    # we also use this technique in checking if a number is a prime, you can find it
    # in is_prime.py file

    while i * i <= N: 
        if is_prime_arr[i]: 

            # if previously we haven't found any factors of a number that are less than it
            # (is_prime_arr for this number remained True)
            # it means it must be prime, because we have checked every possible factors before

            primes_arr.append(i)

            # for our prime number we mark all its multiples as not prime, thus +i in each step
            # we do it only for prime numbers, because for non-primes it isn't necessary
            # because their multiples will be marked by their prime factors

            for j in range(i * i, N+1, i): # We start fron i*i because 2*i, 3*i ...  were already checked by smaller factors
                is_prime_arr[j] = False
        i += 1
    
    for i in range(i, N + 1): # adding remaining primes greater than sqrt(N)
        if is_prime_arr[i]:
            primes_arr.append(i)

    return primes_arr


def eratostenes_optimized(N): # avoids even numbers
    is_prime_arr = [True for _ in range((N//2) + 1)] # only odds
    primes_arr = [2] # we know 2 is prime

    i = 3
    while i * i <= N:
        if is_prime_arr[i//2]: # we store only odds, so index is i//2, for example 3, 5, 7, 9 are stored at 1, 2, 3, 4 indexes respectively
            primes_arr.append(i)
            for j in range(i * i, N + 1, i * 2): # step by i*2 to avoid even multiples
                is_prime_arr[j//2] = False # same case with indexing
        i += 2 # skip even numbers

    for i in range(i, N + 1, 2): # adding remaining primes greater than sqrt(N)
        if is_prime_arr[i//2]:
            primes_arr.append(i)

    return primes_arr


for n in [10, 50, 100, 200]:
    print("-" * 100)
    print("N =", n)
    res = eratostenes(n)
    print(res)
    print("are equal:", eratostenes_optimized(n) == res)
