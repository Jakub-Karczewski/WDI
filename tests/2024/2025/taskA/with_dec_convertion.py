def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def change_base(n, k):
    mult = 1
    nr = 0
    while mult < n:
        nr += 1
        mult *= k

    if mult != n:
        mult //= k
    
    converted = [0 for _ in range(nr)]

    for i in range(nr):
        x = n//mult
        converted[i] = x
        n -= mult * x
        mult //= k
    
    return converted

def calculate_decimal(tab:list[int], k:int) -> int:
    dl = len(tab)
    res = 0
    pow = 1
    for i in range(dl-1, -1, -1):
        res += tab[i] * pow
        pow *= k
    return res


def solve(N):
    act_max_res = 0
    act_best_base = -1
    for b in range(2, 17):
        conv:list[int] = change_base(N, b)
        for i in range(1, len(conv), 1):

            left = conv[:i]
            right = conv[i:]

            left_dec = calculate_decimal(left, b)
            right_dec = calculate_decimal(right, b)
            res = left_dec * right_dec
            if gcd(left_dec, right_dec) == 1 and res > act_max_res:
                act_max_res = res
                act_best_base = b

                print(b)
                print(left, right)
                print(f"{left_dec} * {right_dec} = {act_max_res}")

    print(f"Otrzymana najlepsza podstawa: {act_best_base}")
    print(f"Otrzymany dla niej wynik: {act_max_res}")


N = 202
for n1 in [141, 202, 10092392]:
    print("-" * 100)
    print(f"LICZBA: {n1}")
    solve(n1)
    print("\n")