from collections import deque

def water_jug(cap1, cap2, target):
    queue = deque([(0, 0)])
    visited = set()

    while queue:
        a, b = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        print(a, b)

        if a == target or b == target:
            print("Target reached!")
            return

        x = min(a, cap2 - b)
        y = min(b, cap1 - a)

        states = [
            (cap1, b),
            (a, cap2),
            (0, b),
            (a, 0),
            (a - x, b + x),
            (a + y, b - y)
        ]

        for state in states:
            if state not in visited:
                queue.append(state)

    print("Solution not found")


water_jug(4, 3, 2)
