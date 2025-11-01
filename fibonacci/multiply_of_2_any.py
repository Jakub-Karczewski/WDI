def fib_product(N):
    if N == 1:
        print("1 = 1 * 1")
        return True
    fib_arr = [1, 1]
    while fib_arr[-1] <= N:
        fib_arr.append(fib_arr[-1] + fib_arr[-2])
        act = fib_arr[-1]
        for i in range(len(fib_arr)-1, -1, -1): # we also check the element with itself
            prev = fib_arr[i]
            if prev * act < N:
                break # smaller number will not work either, so we break the loop
            if prev * act == N:
                return True
    return False


def fib_product_optimized(N):
    if N == 1:
        print("1 = 1 * 1 (Fib numbers)")
        return True
    
    fib_arr = [1, 1]

    while True:
        fib_arr.append(fib_arr[-1] + fib_arr[-2])

        if fib_arr[-1] > N:
            break
        
        act = fib_arr[-1]
        if act * 1 == N or act * act == N:
            if N == act * act:
                print(f"{N} = {act} * {act} (Fib numbers)")
            else:
                print(f"{N} = {act} * {1} (Fib numbers)")
            return True
        
        left, right = 0, len(fib_arr) - 1
        while left <= right:
            mid = (left + right)//2
            if fib_arr[mid] * act == N:
                print(f"{N} = {act} * {fib_arr[mid]} (Fib numbers)")
                return True
            if fib_arr[mid] * act > N:
                right = mid-1
            else:
                left = mid+1
        
    return False

for n in [2 * 5, 34 * 3, 55 * 1 , 24 * 55, 89 * 144, 1000, 1597 * 2584]:
    print("-" * 100)
    print("N =", n)
    print(fib_product(n))
    print(fib_product_optimized(n))