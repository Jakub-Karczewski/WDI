K = 10 # maximum number of components, used only for initializing 'splitted' array

splitted = [-1 for _ in range(K)]
last_idx = 0

global count
count = 0

def print_without(tab, limit):
    print("(", end = '')
    for i in range(limit):
        if tab[i+1] == -1 or i == limit-1:
            print(f"{tab[i]})")
            return
        print(f"{tab[i]},", end = ' ')
    

# our recursion will go monotonically, starting from curr_num = 1
# for each natural number it will try to include it one or more times before going to next iteration, this way our splitting will always be monotonic
# We do not need to use backtracking here, because numbers will be overwritten here in 'splitted' array, that's magic of recursion xd

def split_number(n, k, curr_num, last_idx, initial_k): # initial_k will not change, it is only useful for printing results
    global count
    if k == 0: # if there are no components left
        if n == 0: # if number was fully splitted
            count += 1
            print_without(splitted, initial_k)
        return
    if k * curr_num > n: # If it is impossible to form number n using k numbers that are greater of equal to curr_num
        return
    
    split_number(n, k, curr_num+1, last_idx, initial_k) # skip checking current number,
    # if we switch this line with the for loop, the splittings will be printed from smallest to greatest lexicographically

    for i in range(1, k+1): # take current number from 1 to k times
        splitted[last_idx + (i - 1)] = curr_num
        split_number(n - i * curr_num, k-i, curr_num + 1, last_idx + i, initial_k) # recursion for number greater by 1

def stirling(n, k, last_idx, initial_k, add_to_nonempty:list[int]):
    pass

for N1, K1 in [(23, 5), (17, 4), (11, 3), (7, 2)]:
    print("-" * 100)
    print(f"P({N1}, {K1})")
    print("-" * 100)

    print()
    split_number(N1, K1, 1, 0, K1)
    print()
    print(f"FOUND SPLITTINGS: {count}\n")

    count = 0

# Stirling will be implemented in the future




