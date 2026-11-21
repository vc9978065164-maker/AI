
import heapq

maze = [
    ['S', '.', '.', '#'],
    ['#', '#', '.', '#'],
    ['.', '.', '.', '.'],
    ['#', '#', '#', 'G']
]

start = (0, 0)
goal = (3, 3)

def heuristic(position):
    x, y = position
    return abs(x - goal[0]) + abs(y - goal[1])

def solve_maze():
    queue = [(heuristic(start), 0, start, [start])]
    visited = set()

    while queue:
        f, cost, current, path = heapq.heappop(queue)

        if current == goal:
            return path
        if current in visited:
            continue

        visited.add(current)
        x, y = current

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if (0 <= nx < 4 and 0 <= ny < 4
                and maze[nx][ny] != '#'
                and (nx, ny) not in visited):

                new_cost = cost + 1
                priority = new_cost + heuristic((nx, ny))
                heapq.heappush(
                    queue,
                    (priority, new_cost, (nx, ny), path + [(nx, ny)])
                )

    return None


path = solve_maze()

if path:
    print("Path found:")
    for position in path:
        print(position)
    print("Total steps:", len(path) - 1)
else:
    print("No path found")
