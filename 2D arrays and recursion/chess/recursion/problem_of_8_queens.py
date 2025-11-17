# The problem is to place 8 queens on an 8x8 chessboard such that no two queens threaten each other.
# This means that no two queens can be in the same row, column, or diagonal.
# First we need to create arrays that will represent every row, column and diagonal on the chessboard.
# our recursion will go by rows, one by one, and try to place a queen in every column that is not threatened by another queen.
# When finishing recursive call for current call, after all its subcalls returned, we will undo the move
# Because when we try next column in that row, we don't want our arrays to still store the information for the previously placed 
# queen, there can be only queen one per row and our recursive call ended its job, so we do not need it anymore
# Also, when it comes to diagonals, we can see that all elements on the same DOWN diagonal share the same row_id - col_id
# For DOWN diagonals, possible differences range from -(n-1) to (n-1), thus for indexing we need to add n-1 to result to have indexing from 0
# On the other hand, elements on the same UP diagonal, share the same row_id + col_id, and the possible values are between 0 and 2 * (n-1)


n = 8 # number of rows and columns
rows_arr, cols_arr, diagonals_down, diagonals_up = [0 for _ in range(n)], [0 for _ in range(n)], [0 for _ in range(2*n - 1)], [0 for _ in range(2*n - 1)]
board = [[0 for _ in range(n)] for _ in range(n)]

def is_safe(row, col):
    return rows_arr[row] == 0 and cols_arr[col] == 0 and diagonals_up[row + col] == 0 and diagonals_down[row - col + (n-1)] == 0

def change_arrays(row, col, fill = 1): # fill parameter will be 1 by default, when fill = 0 that means we undo our move
    rows_arr[row], cols_arr[col], diagonals_up[row + col], diagonals_down[row - col + (n-1)] = fill, fill, fill, fill
    board[row][col] = fill


global sols
sols = 1

def place_queen(row):
    global sols

    if row == n: # the end condition for recursion, we placed all queens correctly, and called recursively for row after last
        print("-" * 100)
        print(f"SOLUTION NR {sols}\n")
        print(*board, sep = "\n")
        print()
        sols += 1
        return
    
    for col in range(n):
        if is_safe(row, col):
            change_arrays(row, col, 1) # placing queen
            place_queen(row + 1) # recursive call for next row
            change_arrays(row, col, 0) # undo the move - BACKTRACKING

    return 


# we can change n to see results for different sizes, it is 8 by default

place_queen(0)

print("-" * 100)
print(f"TOTAL SOLUTIONS: {sols - 1}")
print("-" * 100 + "\n")

