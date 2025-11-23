# We have a knapsack that can hold a maximum weight of W
# We have n items, each with a weight weight[i] and a value val[i]
# Our golal is to maximize the value we can carry in the knapsack without exceeding the weight W
# First idea is to use recursion to try all possible combinations of items
# For every item, we have two choices: either include it in the knapsack or exclude it
# We will explore both choices recursively and keep track of the maximum value we can achieve
# We will also use backtracking to keep track of items we chose along the way
# This approcach gives us 2^n complexity, that is a lot, but enough for 1st year students XD

# There exists a way to optimize our calculations, if the weights are integers and not too large using memoization
# We can observe, that we have W * n possible states (remaining weight and current item index)
# During our recursion, we call the same state multiple times
# We can store the results of these states in a memoization table to avoid redundant calculations
# When we encounter the same state again, we can simply return the stored result instead of recalculating it

import random

n = 3
W = 30

weights = [random.randint(6, W//2) for _ in range(n)]
values = [random.randint(5, 30) for _ in range(n)]


def get_taken_idxs(taken_paths):
    taken_filtered = [i for i,x in enumerate(taken_paths) if taken_paths[i]]
    return taken_filtered


def knapsack_naive(W, idx, curr_val):
    if idx == -1: # all elements were considered
        return curr_val, [False for _ in range(n)] # we are returning value and path that led to this value, in order to recreate answer later
    
    take, taken_paths1 = 0, []

    if weights[idx] <= W: # the item fits, so we can take it
        take, taken_paths1 = knapsack_naive(W - weights[idx], idx - 1, curr_val + values[idx]) # first recursive call

    dont_take, taken_paths2 = knapsack_naive(W, idx - 1, curr_val) # we skip the element, second recursive call

    # we keep track of chosen elements by doing it from the back, we store it in taken_paths arrays
    # because only after recursive calls ended, we can say, which option was better

    if take > dont_take:
        taken_paths1[idx] = True # we know taking element on this index was better
        return take, taken_paths1
    
    taken_paths2[idx] = False
    return dont_take, taken_paths2


#---------------------------------------------------------------------
#               Optimized version with memoization
#---------------------------------------------------------------------
mem = [[-1 for _ in range(W+1)] for _ in range(n)] # memoization table
parents = [[[-1, -1] for _ in range(W+1)] for _ in range(n)] 

def knapsack_better(W, idx, curr_val):
    if idx == -1:
        return curr_val
    if mem[idx][W] != -1:
        return mem[idx][W]
    
    take = 0
    if weights[idx] <= W: 
        take = knapsack_better(W - weights[idx], idx - 1, curr_val + values[idx]) 
        parents[idx][W][0], parents[idx][W][1] = idx - 1, W - weights[idx]

    dont_take = knapsack_better(W, idx - 1, curr_val)
    if dont_take > take:
        parents[idx][W][0], parents[idx][W][1] = idx-1, W # we overwrite parent, because there is better

    return max(take, dont_take)

    

print(f"\nW = {W}")
print(f"weights = {weights}")
print(f"values = {values}\n")

best_res, best_path = knapsack_naive(W, n-1, 0)
print(f"BEST RES: {best_res}")

taken_idxs = get_taken_idxs(best_path)
print("TAKEN ELEMENTS:", taken_idxs)
print()


best_res_mem = knapsack_better(W, n-1, 0)
print(f"BEST RES OPTIMIZED: {best_res_mem}")
act = [n-1, W]
prev = [n-1, W]
taken_elems = []

while True:
    act = parents[act[0]][act[1]]
    if prev[1] != act[1]: # we took this elements, weight decreased
        taken_elems.append(prev[0])
    
    if act[0] == -1:
        break
    prev[0], prev[1] = act[0], act[1]

print(f"TAKEN: {taken_elems[::-1]}")

assert best_res == best_res_mem




