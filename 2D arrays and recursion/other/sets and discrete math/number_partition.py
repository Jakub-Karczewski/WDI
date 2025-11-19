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
# for each natural number it will try to include it one or more times before going to next iteration,
# this way elements in each partition will always be monotonic
# We do not need to use backtracking here, because numbers will be overwritten in 'splitted' array
# And the result will still be valid, that's magic of recursion xd

def split_number(n, k, curr_num, last_idx, initial_k): # initial_k will not change, it is only useful for printing results
    global count

    if k == 0: # if there are no components left
        if n == 0: # if number was fully splitted, otherwise our partition is invalid
            print_without(splitted, initial_k)
            count += 1
        return
    
    if k == 1: # we have only one component left
        if n >= curr_num: # checking if it fits or would fit in the future
            splitted[last_idx] = n # this if is useful if we have many small numbers at the beginning and the last is large
            print_without(splitted, initial_k)
            count += 1
        return
    
    if k * curr_num > n: # If it is impossible to form number n using k numbers that are greater of equal to curr_num
        return
    
    split_number(n, k, curr_num+1, last_idx, initial_k) # skip checking current number,
    # if we switch this line with the for loop, the possible partitions will be printed from smallest to greatest lexicographically

    for i in range(1, k+1): # take current number from 1 to k times
        splitted[last_idx + (i - 1)] = curr_num
        split_number(n - i * curr_num, k-i, curr_num + 1, last_idx + i, initial_k) # recursion for number greater by 1


for N1, K1 in [(23, 5), (17, 4), (11, 3), (7, 2)]:
    print("-" * 100)
    print(f"P({N1}, {K1})")
    print("-" * 100)

    print()
    split_number(N1, K1, 1, 0, K1)
    print()
    print(f"FOUND SPLITTINGS: {count}\n")

    count = 0