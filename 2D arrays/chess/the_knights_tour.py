def check_sanity(row, col, size_row, size_col):
    return (0 <= row <= size_row - 1) and (0 <= col <= size_col - 1)

def knights_tour(row, col, id, visited):
    visited[row][col] = id
    size_row, size_col = len(visited), len(visited[0])

    if id == size_row * size_col: # last field on board fullfilled
        return True, id
    
    moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]
    maxi = id # this is out potential maximum, we cannot get less than that in this recusrion subtree

    for move_row, move_col in moves:
        act_row, act_col = row + move_row, col + move_col
        if check_sanity(act_row, act_col, size_row, size_col) and visited[act_row][act_col] == 0:
            res, max_id = knights_tour(act_row, act_col, id+1, visited)
            maxi = max(maxi, max_id)
            if res:
                return True, maxi # in this case maxi has to be size_row * size_col

    visited[row][col] = 0 # backtracking
    return False, maxi


for (n, m) in [(3, 3), (5, 5), (7, 7)]:
    vis = [[0 for _ in range(m)] for _ in range(n)]
    print("-" * 100)
    print(f"n, m = ({n}, {m})")

    valid, max_visited = knights_tour(0, 0, 1, vis)

    if valid:
        print("Success\n")
        print(*vis, sep="\n")
    else:
        print("Did not manage to travel whole board")
        print(f"Maximum fields visited: {max_visited}")
    print()