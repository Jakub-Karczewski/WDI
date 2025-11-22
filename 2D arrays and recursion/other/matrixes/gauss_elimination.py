# We assume squared matrix for convenience
import random
import math
n = 6
M = [[random.randint(0, 9) for _ in range(n)] for _ in range(n)]

def swap_rows(row1, row2):
    for j in range(n):
        M[row1][j], M[row2][j] = M[row2][j], M[row1][j]


def divide_row(row, k):
    for j in range(n):
        M[row][j] /= k

def add_scaled_row_to_another(row1, row2, k):
    for j in range(n):
        M[row2][j] += M[row1][j] * k

def gauss_elimination():
    for j in range(n): # we go by every column to try to create stairs
        maxi, pivot_idx = 0.0, 0 # pivot is the row we are planning to swap with our current
        for i in range(j, n):
            # we search for the largest in abs value element in column j, because we do not want to divide by small numbers, it creates numerical errors
            if abs(M[i][j]) > maxi :
                maxi, pivot_idx = abs(M[i][j]), i

        if pivot_idx != j: # we need to swap
            swap_rows(j, pivot_idx)

        divide_row(j, M[j][j]) # we want our row to have 1.0 as the element on the diagonal

        for k in range(j + 1, n):
            add_scaled_row_to_another(j, k, -M[k][j]) # we 'zero' all the elements below element on diagonal


def print_matrix():
    for row in M:
        row_rounded = [round(x, 2) for x in row]
        row_no_negative_zeros = [0.0 if math.isclose(x, 0.0) else x for x in row_rounded]
        print(" ".join(f"{x:.2f}" for x in row_no_negative_zeros))
    print()

print()
print_matrix()
print("\nAFTER GAUSS ELIMINATION:\n")
gauss_elimination()
print_matrix()