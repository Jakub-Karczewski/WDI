import random
import numpy as np
import math

n = 6
M1 = [[random.randint(0, 15) / 2 for _ in range(n)] for _ in range(n)]

# M1 = [
#     [0, 1, 2, 7],
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [-1 , 1, -1, 1]
# ]
# example from wikipedia

def get_column(M, col):
    return [M[i][col] for i in range(len(M))]


def get_sign(row, col):
    return 1 if (row + col) % 2 == 0 else -1

excl_cols = [False for _ in range(n)]

# We will go from row 0 to n-1, and 'remove' rows from top to bottom and for each row we will traverse columns from left to right
# We will not keep track for remaining number zeros in each row and col for optimalization, because it currently complicates our solution a lot
def find_determinant(row):
    if row == n-1: # this can be replaced with end conditions for 2x2 and 3x3 matrixes
        for col in range(n):
            if not excl_cols[col]: # searching for the remaining, not excluded column
                return M1[n-1][col]
    

    # number of excluded rows is equal to the number to excluded cols and it is n - row
    # And in our algortihm we cut the rows from the top so every time considered row will have index 0, bacause we change indexing after removing rows
    # So the sign will only depend on col index

    res = 0
    col_id = 0 # we also change indexing for columns
    for col in range(n):
        if not excl_cols[col]:
            excl_cols[col] = True
            res += M1[row][col] * get_sign(0, col_id) * find_determinant(row+1)
            col_id += 1 # update index after finding not excluded col
            excl_cols[col] = False # backtracking


    # -----------------------------------------------------------------------
    #    THIS CODE IS ONLY USEFUL TO SEE WHAT IS GOING ON INSIDE RECURSION
    # -----------------------------------------------------------------------
    # temp_matrix = [[0 for _ in range(n-row)] for _ in range(n-row)]
    # for r in range(row, n):
    #     col_id = 0
    #     for col in range(n):
    #         if not excl_cols[col]:
    #             temp_matrix[r-row][col_id] = M1[r][col] 
    #             col_id += 1
    # print("Act matrix:", *temp_matrix, sep = "\n")
    # print("Res:", res)

    return res



numpy_det = np.linalg.det(np.array(M1)) # determinant using library function to compare result
rec_det = find_determinant(0)
print(rec_det)

assert math.isclose(numpy_det - rec_det, 0.0, abs_tol=1e-6)
    
    