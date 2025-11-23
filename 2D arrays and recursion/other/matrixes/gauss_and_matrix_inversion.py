# We assume squared matrix for convenience
import random
import math
import numpy as np
import copy

def print_matrix(M):
    for row in M:
        row_rounded = [round(x, 2) for x in row]
        row_no_negative_zeros = [0.0 if math.isclose(x, 0.0) else x for x in row_rounded]
        print(" ".join(f"{x:.2f}" for x in row_no_negative_zeros))
    print()


def divide_row(row, k, M):
    n = len(M)
    for j in range(n):
        M[row][j] /= k


def swap_rows(row1, row2, M):
    n = len(M)
    for j in range(n):
        M[row1][j], M[row2][j] = M[row2][j], M[row1][j]


def add_scaled_row_to_another(row1, row2, k, M):
    n = len(M)
    for j in range(n):
        M[row2][j] += M[row1][j] * k


def gauss_elimination(M):
    n = len(M)
    for j in range(n): # we go by every column to try to create stairs
        maxi, pivot_idx = 0.0, 0 # pivot is the row we are planning to swap with our current
        for i in range(j, n):
            # we search for the largest in abs value element in column: j below row: j, because we do not want to divide by small numbers, it creates numerical errors
            if abs(M[i][j]) > maxi :
                maxi, pivot_idx = abs(M[i][j]), i # updating pivot

        if pivot_idx != j: # we need to swap
            swap_rows(j, pivot_idx, M)

        divide_row(j, M[j][j], M) # we want our row to have 1.0 as the element on the diagonal, because this way we can easily find the multiplier for adding this row to rows below

        for k in range(j + 1, n):
            add_scaled_row_to_another(j, k, -M[k][j], M) # we 'zero' all the elements below element on diagonal for column j


# We are going to use Gauss-Jordan elimination 
def inverse_matrix(M):
    n = len(M)
    M_res = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        M_res[i][i] = 1
    
    for j in range(n):
        maxi, pivot_idx = 0.0, 0 
        for i in range(j, n):
            if abs(M[i][j]) > maxi :
                maxi, pivot_idx = abs(M[i][j]), i 

        if pivot_idx != j:
            swap_rows(j, pivot_idx, M)
            swap_rows(j, pivot_idx, M_res)

        div = M[j][j]
        divide_row(j, div, M) 
        divide_row(j, div, M_res)

        for k in range(n):
            if k != j:
                scalar = -M[k][j]
                add_scaled_row_to_another(j, k, scalar, M) 
                add_scaled_row_to_another(j, k, scalar, M_res)

    return M_res


def find_determinant(M):
    pass


n = 6
M1 = [[random.randint(0, 15) for _ in range(n)] for _ in range(n)]
M2 = copy.deepcopy(M1) # because operations on M1 are done in place, that's current design of functions


print()
print_matrix(M1)
print("\nAFTER GAUSS ELIMINATION:\n")
gauss_elimination(M1)
print_matrix(M1)


if np.linalg.det(np.array(M2)) != 0: # For now using external library to check, if a matrix can be inversed
    print("\nINVERSE MATRIX\n")
    print_matrix(inverse_matrix(M2))
