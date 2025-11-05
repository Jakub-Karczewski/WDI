def string_to_char_arr(S:str):
    n = len(S)
    s_arr:list[str] = ['a' for _ in range(n)]

    for i in range(n):
        s_arr[i] = S[i]

    return s_arr

def get_substr(s_arr:list[str], i, j):
    res_arr = ['a' for _ in range(j - i + 1)]
    for k in range(i, j+1):
        res_arr[k-i] = s_arr[k]
    return res_arr


def get_repeated_substring(S):
    n = len(S)
    s_arr = string_to_char_arr(S)
    print("Przeksztalcony:", s_arr)
    for i in range(n//2, 0, -1):
        if n % i != 0: # len of full string not divisible by len of our candidate
            continue
        candidate = get_substr(s_arr, 0, i-1) # first i characters
        len_cand = i
        number_of_reps = n//i

        ok = True
        for k in range(1, number_of_reps):
            for j in range(len_cand):
                pos_in_s = k * len_cand + j
                if s_arr[pos_in_s] != candidate[j]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            print(f"Najlepszy znaleziony: {candidate}, jego len: {len(candidate)}")
            break
    
dupa = "ABCABCABCABC"
print("rozpatrywany napis:", dupa)
get_repeated_substring(dupa)