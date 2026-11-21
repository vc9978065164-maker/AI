def dfs_water_jug(cap1, cap2, target):
    visited = set()

    def dfs(a, b):
        if (a, b) in visited:
            return False

        visited.add((a, b))
        print(a, b)

        if a == target or b == target:
            print("Target reached!")
            return True

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

        for next_a, next_b in states:
            if dfs(next_a, next_b):
                return True
        return False

    if not dfs(0, 0):
        print("Solution not found")


dfs_water_jug(4, 3, 2)
