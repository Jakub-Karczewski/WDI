def prime_factorization(N):
    prime_factors = []
    if N <= 1:
        return []
    for f in [2, 3, 5]: # first we factor by 2, 3, 5 in order to check later others with +6 method
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
    print("last i:", i)

    # N > 1 means that our number either is prime, because it was not factorized,
    # or was partially factorized and one of the factor is large enough to not be checked before

    if N > 1:
        prime_factors.append([N, 1])
    return prime_factors

def format_factors_print(N, prime_factors):
    print(f"{N} =", end = ' ')
    for i in range (len(prime_factors)):
        f, count = prime_factors[i]
        print(f"{f}^{count}", end = ' ')
        if i < len(prime_factors) - 1:
            print("*", end = ' ')

for n in [10, 28, 50, 97, 100, 121, 169, 200, 256, 997, 1000]:
    factors = prime_factorization(n)
    format_factors_print(n, factors)
    print("\n" + "-" * 100)