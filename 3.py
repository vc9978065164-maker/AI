def dfs(start, goal, limit=20):
    visited = set()

    def search(state, path, depth):
        if state == goal:
            return path + [state]
        if depth == limit:
            return None

        visited.add(state)
        zero = state.index(0)
        moves = [-1, 1, -3, 3]

        for move in moves:
            new_pos = zero + move

            if new_pos < 0 or new_pos > 8:
                continue
            if move == -1 and zero % 3 == 0:
                continue
            if move == 1 and zero % 3 == 2:
                continue

            new_state = list(state)
            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )
            new_state = tuple(new_state)

            if new_state not in visited:
                result = search(new_state, path + [state], depth + 1)
                if result:
                    return result

        return None

    return search(start, [], 0)


start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

result = dfs(start, goal)

if result:
    for state in result:
        print(state[:3])
        print(state[3:6])
        print(state[6:])
        print()
    print("Steps:", len(result) - 1)
else:
    print("Solution not found")
