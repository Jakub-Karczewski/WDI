def multiply_of_adjacent_fibonacci(N):
    if N <= 0:
        return False
    if N == 1:
        return True
    a, b = 1, 1

    while a * a <= N: # we can stop when a^2 > N, because b > a, so a*b > a^2
        a, b = b, a + b
        if a * b == N:
            print(f"{N} = {a} * {b} (Fibonacci numbers)")
            return True
    return False

for n in [0, 1, 2, 3, 4, 5, 6, 14, 15, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]:
    print("-" * 100)
    print("N =", n)
    print(multiply_of_adjacent_fibonacci(n))