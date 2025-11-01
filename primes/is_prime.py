def is_prime_optimized(N):

    # Let our first observation be that if we look at all the mod 6 rests
    # we can see that 0, 2, 4 definitely are not primes, because they are even (we skip checking number 2, because it is prime)
    # also 3 cannot be prime, but that implies division by 3 (we skip checking number 3 because it is prime)
    # So we are left only with rests 1 and 5 
    # e.g 7, 11, 13, 17, 19, 23, 25, 29 (we skip checking 5 in a loop for simplification, we check her before, with 2 and 3)
    # Not all these numbers are obviously primes, but they are candidates for being prime factors of our number
    # we can see that the differences between these numbers are 2 and 4 alternately
    # we can optimize finding them and instead of using flag, whether we need to add 2 or 4,
    # we can add 6 in each iteration starting from 6 and check both numbers, one is +1, other is +5

    if N <= 1:
        return False
    if N in [2, 3, 5]:
        return True
    if N % 2 == 0 or N % 3 == 0 or N % 5 == 0:
        return False
    
    i = 6
    while i * i <= N:
        print(i+1, i+5, end=' ')
        if N % (i+1) == 0 or N % (i+5) == 0:
            return False
        i += 6
    return True

for n in [1, 2, 3, 4, 5, 10, 13, 25, 29, 97, 100, 121, 169, 200, 997]:
    print("-" * 100)
    print(f"Checking if {n} is prime:")
    a = is_prime_optimized(n)
    print(f"\n\nIs {n} prime? -> {a}")