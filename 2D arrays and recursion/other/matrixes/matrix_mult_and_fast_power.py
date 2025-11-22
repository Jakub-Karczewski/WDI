def matrix_mult(M1 :list[list[float | int]], M2 :list[list[float | int]]):

    w1, k1 = len(M1), len(M1[0])
    w2, k2 = len(M2), len(M2[0])
    assert k1 == w2, f"matrix with {k1} columns cannot be multiplied with matrix with {w2} rows"

    w3, k3 = w1, k2 # dims of a result matrix
    M3 = [[0 for _ in range(k3)] for _ in range(w3)]

    inner = k1 # also w2
    for i in range(w1):
        for j in range(k2):
            for p in range(inner):
                M3[i][j] += M1[i][p] * M2[p][j] # we iterate over i-th row of M1 and j-th column of M2 at the same time
    return M3


def multiply_vecs(vec1 : list[float | int], vec2 : list[float | int]):
    assert len(vec1) == len(vec2)

    n1 = len(vec1)
    res = [0 for _ in range(n1)]
    for i in range(n1):
        res[i] = vec1[i] * vec2[i]
    return res


# elem can be number, vector or square matrix, expressions after : in arguments list are only TYPE HINTS
def multiply_elems(elem1: float | int | list[float | int] | list[list[float | int]], elem2: float | int | list[float | int] | list[list[float | int]]): 

    if type(elem1) in [float, int]: # number
        return elem1 * elem2
    
    if type(elem1) == list and type(elem1[0]) != list: # vector
        return multiply_vecs(elem1, elem2)
    
    if type(elem1) == list and type(elem1[0]) == list: # matrix
        return matrix_mult(elem1, elem2)

# Let's say we want raise 2 to the power of 15
# The first solution that probably comes to mind is multiplying result by 2 in a loop 15 times
# But what if there is other, more efficient way, that would require a lot less multiplications
# Our first observation is that, when we square some number it is the same as binary shift of a power
# e.g. (3^5)^2 = 3^10, in binary system 5 = 101, 10 = 1010

# 15 is 1111 in binary system
# let's start with the leftmost digit of binary number and try recreate our power with binary shifs (squaring the number)
# BIN: 1, 2^1 = 2, POW: 1
# BIN: 10, (2)^2 = 4, POW: 2, still we can see that our number has 1 on the second position from the left, thus we multiply by 2^1
# BIN: 11, 4 * 2^1 = 8, POW: 3
# BIN: 110, (8)^2 = 64, POW: 6, same situtation as above, we need to multiply
# BIN: 111, 64 * 2^1 = 128, POW: 7
# BIN: 1110, (128)^2 = 16384, POW: 14
# BIN: 1111, 16384 * 2^1 = 32768, POW: 15

# We can see that it required us log2(n) multiplications to calculate our number
# And the only thing we need to know is the remainer mod 2 of the current number
# We can use recursion in this case
# If we called recursive change to binary system (with // 2 and % 2) we could achieve this
# And due to recursion property, we could start building our solution from the back, this means our last recursive call would be for n = 1
# 15 (1) => 7 (1) => 3 (1) => 1 (1), numbers in parenthesis are the remainders mod 2
# And every time our remainder is 1, we multiply our number additionally by our base, and return result recursively from the bottom


def fast_power(elem: float | int | list[float | int] | list[list[float | int]], k: int): # elem can be number, vector or square matrix, k is a current power
    if k == 0: # only for case a ^ 0
        return 1 # we assume we will not raise vector or matrix to the power of 0, only number
    
    if k == 1: # end state of recursion
        return elem
    
    res = fast_power(elem, k // 2) # recursive call
    res_sq = multiply_elems(res, res) # we square our result => binary shift of a power

    if k % 2 == 1:
        res_sq = multiply_elems(res_sq, elem) # we multiply additionally by our base if needed
   
    return res_sq


# multiplying by base in a for loop
def naive_power(elem: float | list[float] | list[list[float]], k:int):
    if k == 0:
        return 1 # same assumption
    
    res = elem
    for i in range(k - 1):
        res = multiply_elems(res, elem)
    return res


print("\nPOWERS OF INTEGERS:\n")
# Comparing results for fast power and standard power raising
for n, k in [(2, 15), (3, 17), (5, 100)]:
    res = fast_power(n, k)
    print(f"{n} ^ {k} = {res}")
    print(f"Equal: {res == naive_power(n, k)}\n")
    

# --------------------------------------------------------------------
#      Trick for calculating n-th fibonacci number in log2(n) time
# --------------------------------------------------------------------

# raising [ [1, 1, [1, 0]] ] to n-th power gives us:
#  [ 
#   [ fib[n+1], fib[n] ],
#   [ fib[n], fib[n-1] ]
#  ] 
# array

fib_M = [ [1, 1],
          [1, 0 ] ]

print("\nFIBONACCI NUMBERS:\n")
for N in [3, 5, 7, 15, 100]:
    res_fib = fast_power(fib_M, N)
    print(f"N = {N}")
    if N < 20:
        print(res_fib)
    else:
        print(res_fib[0][1])
    print()

    
