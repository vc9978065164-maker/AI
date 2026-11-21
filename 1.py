from collections import deque

def bfs(start, goal):
    queue = deque([(start, [])])
    visited = {start}
    moves = [-1, 1, -3, 3]

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        zero = state.index(0)

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
                visited.add(new_state)
                queue.append((new_state, path + [state]))

    return None


start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

result = bfs(start, goal)

if result:
    print("Solution found:")
    for state in result:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
    print("Total steps:", len(result) - 1)
else:
    print("No solution found")
