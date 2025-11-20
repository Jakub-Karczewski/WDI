# For now this code is obscure and needs to be refactored but works fine

# We will try to implement basic idea behind stirling partition coming from discrete maths
# There is a formula for Stirling 2nd kind: S(n, k) = S(n-1, k-1) + k * S(n-1, k)
# First case is a situation when element is alone in a group, second is a case when we append it to one of nonempty sets
# First observation is that, for sure recursion will go by each element (parameter n), but still remains the case of k and appending to sets
# The easiest way to do so, is the store the elements that are waiting for appending and the index of a block, at which they appeared

global count
count = 0

def get_elems_and_limits(T):
    elems, limits = [-1 for _ in range(len(T))], [-1 for _ in range(len(T))]

    for i in range(len(T)):
        x, y = T[i]
        if x == -1:
            return elems, limits, i

        elems[i], limits[i] = x, y

    return elems, limits, len(T)


max_N = 30
max_K = 10

numbers_to_append = [[-1, -1] for _ in range(max_N)]
last_idxs_main = [0 for _ in range(max_N)]
blocks = [[-1 for _ in range(max_N)] for _ in range(max_K)]


def print_blocks(larger_blocks, max_row):
    global count
    count += 1
    row, col = max_row, len(larger_blocks[0])

    print("[", end = '')
    for i in range(row):
        print("(", end = '')
        for j in range(col):
            if j == col-1 or larger_blocks[i][j+1] == -1:
                print(f"{larger_blocks[i][j]})", end = '')
                break
            print(f"{larger_blocks[i][j]}, ", end = '')

        if i < row - 1:
            print(", ", end = '')

    print("]")


def permutations(elems, limits, N1, K1):
    import copy
    
    last_idxs = copy.deepcopy(last_idxs_main) # we copy this array, because there is no point in messing with indexing and modifying content, that is used in 'stirling' func
    blocks_inner = copy.deepcopy(blocks) 

    def permute(n):
        if n == 0:
            print_blocks(blocks_inner, K1 + 1)
            return
    
        for k in range(limits[n-1], K1+1):

            blocks_inner[k][last_idxs[k]] = elems[n-1]
            last_idxs[k] += 1

            permute(n-1)

            last_idxs[k] -= 1
            blocks_inner[k][last_idxs[k]] = -1 # backtracking

    permute(N1)


def stirling(n, k, max_k, last_idx):

    if max_k - k + 1 > n:
        return
    
    if k == max_k + 1:
        if n == 0:
            elems, limits, to_append = get_elems_and_limits(numbers_to_append)
            permutations(elems, limits, to_append, max_k)
        return
    
    if k == max_k:
        for i in range(n):
            blocks[max_k][last_idxs_main[max_k]] = i
            last_idxs_main[max_k] += 1

        elems, limits, to_append = get_elems_and_limits(numbers_to_append)
        permutations(elems, limits, to_append, max_k)

        for i in range(n-1, -1, -1):
            last_idxs_main[max_k] -= 1
            blocks[max_k][last_idxs_main[max_k]] = -1

        return
    

    blocks[k][last_idxs_main[k]] = n-1
    last_idxs_main[k] += 1

    stirling(n-1, k+1, max_k, last_idx)

    last_idxs_main[k] -= 1
    blocks[k][last_idxs_main[k]] = -1

    numbers_to_append[last_idx][0], numbers_to_append[last_idx][1] = n-1, k
    
    stirling(n-1, k, max_k, last_idx+1)

    numbers_to_append[last_idx][0], numbers_to_append[last_idx][1] = -1, -1 # backtracking


for nn, kk in [(3, 2), (6, 3), (9, 2)]:
    print("-" * 100)
    print(f"{" " * 50}S({nn}, {kk})")
    print("-" * 100)

    print()
    stirling(nn, 0, kk-1, 0)
    print()

    print(f"FOUND POSSIBLE SETS: {count}\n")
    count = 0
