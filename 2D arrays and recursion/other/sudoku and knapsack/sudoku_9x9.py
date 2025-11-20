# We have 9x9 sudoku board that is divided into 3x3 sub-boxes
# Previouslt correct board was modified by permutating 3 of the sub-boxes
# The goal is to restore the original board by finding the correct permutation of the 3 sub-boxes
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

def starting_row_col(box_id):
    starting_row = (box_id // 3) * 3
    starting_col = (box_id % 3) * 3
    return starting_row, starting_col


def swap_boxes(box_id1, box_id2, my_board):
    w1, k1 = starting_row_col(box_id1)
    w2, k2 = starting_row_col(box_id2)

    for i in range(3):
        for j in range(3):
            my_board[w1 + i][k1 + j], my_board[w2 + i][k2 + j] = my_board[w2 + i][k2 + j], my_board[w1 + i][k1 + j]

    


def check_sanity():
    import copy
    board_copied = copy.deepcopy(board)
    # if we want to create a permutation e.g out of numbers 1, 5, 6 we need to check all possibilities
    # It will be (1, 5, 6) and (1, 6, 5)


def check_permutations(numbers_left, curr_box_id):
    if numbers_left == 0 or curr_box_id == N:
        return
    
    check_permutations(numbers_left, curr_box_id+1)

    chosen_nums[3 - numbers_left] = curr_box_id
    check_permutations(numbers_left-1, curr_box_id+1)
    chosen_nums[3 - numbers_left] = -1



    