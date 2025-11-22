# We have 9x9 sudoku board that is divided into 3x3 sub-boxes, and each sub-box is also 3x3 valid sudoku
# Previously correct board was modified by permutating 3 of the sub-boxes in a cyclic manner
# The goal is to restore the original board by finding the correct inverse permutation of the 3 sub-boxes
# We are going to give indexes to the boxes the following way:
# 0 1 2 
# 3 4 5
# 6 7 8


def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()


N = 9
K = 3
board = [[0 for _ in range(N)] for _ in range(N)]
chosen_nums = [-1 for _ in range(K)]


def generate_valid_board():
    for i in range(N):
        for j in range(N):
            board[i][j] = ((i * 3 + i//3 + j) % 9) + 1

    # Let's consider 6x6 sudoku
    # For every row from 0 to 2 we start with the element grater by 3 than the starting element of previous row
    # We can say that we move 3 elements in a cycle, that's the effect of i * 3 component

    # 1 2 3 4 5 6
    # 4 5 6 7 8 9
    # 7 8 9 1 2 3

    # Then we move into rows 3-5
    # we can see that they are the same as previous but they are moved by 1 in cycle, because of i//3 component

    # 2 3 4 5 6 7
    # 5 6 7 8 9 1
    # 8 9 1 2 3 4

    # That's basically how it works XD


def validate_sudoku(board):
    # check rows
    for i in range(N):
        seen = [False for _ in range(N+1)] # numbers are from 1 to 9
        for j in range(N): # go over columns for row i
            val = board[i][j]
            if seen[val]: # some value repeated, that implies sudoku is invalid
                return False
            seen[val] = True


    # check columns
    for j in range(N):
        seen = [False for _ in range(N+1)]
        for i in range(N):
            val = board[i][j]
            if seen[val]: 
                return False
            seen[val] = True


    # check boxes
    for box_id in range(9):
        seen = [False for _ in range(N+1)]
        sr, sc = starting_row_col(box_id)

        for i in range(3):
            for j in range(3):
                val = board[sr + i][sc + j]
                if seen[val]: # only if value in box reapeats, sudoku is invalid, because rows and columns were already checked
                    return False
                seen[val] = True

        return True


def starting_row_col(box_id):
    starting_row = (box_id // 3) * 3
    starting_col = (box_id % 3) * 3
    return starting_row, starting_col


def cycle_boxes(a, b, c, my_board):
    # save A
    wa, ka = starting_row_col(a)
    temp = [[my_board[wa+i][ka+j] for j in range(3)] for i in range(3)]

    # A <= C
    wc, kc = starting_row_col(c)
    for i in range(3):
        for j in range(3):
            my_board[wa+i][ka+j] = my_board[wc+i][kc+j]

    # C <= B
    wb, kb = starting_row_col(b)
    for i in range(3):
        for j in range(3):
            my_board[wc+i][kc+j] = my_board[wb+i][kb+j]

    # B <= temp(A)
    for i in range(3):
        for j in range(3):
            my_board[wb+i][kb+j] = temp[i][j]


def check_sanity():
    import copy
    board_copied1 = copy.deepcopy(board)

    # if we want to create a permutation e.g out of numbers 1, 5, 6 we need to check all possibilities
    # It will be (1, 5, 6) and (1, 6, 5)

    cycle_boxes(chosen_nums[0], chosen_nums[1], chosen_nums[2], board_copied1)

    if validate_sudoku(board_copied1):
        print("Found solution")
        print("Chosen inverse permutation", chosen_nums, "\n")
        return True
    

    board_copied2 = copy.deepcopy(board)
    cycle_boxes(chosen_nums[0], chosen_nums[2], chosen_nums[1], board_copied2)

    if validate_sudoku(board_copied2):
        print("Found solution")
        chosen_nums[1], chosen_nums[2] = chosen_nums[2], chosen_nums[1]
        print("Chosen inverse permutation", chosen_nums, "\n")
        return True


def check_permutations(numbers_left, curr_box_id):
    if numbers_left == 0 or curr_box_id == N:
        if check_sanity():
            return True
        return False
    
    if check_permutations(numbers_left, curr_box_id+1):
        return True

    chosen_nums[3 - numbers_left] = curr_box_id
    if check_permutations(numbers_left-1, curr_box_id+1):
        return True
    chosen_nums[3 - numbers_left] = -1

    return False


generate_valid_board()
to_swap = [0, 3, 5]
print("\n")
print(*board, sep="\n")


print("\n")
cycle_boxes(to_swap[0], to_swap[1], to_swap[2], board)


print(*board, sep="\n")
print("\n")
check_permutations(3, 0)