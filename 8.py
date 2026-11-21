def solve_n_queens(n):
    board = [-1] * n

    def is_safe(row, col):
        for i in range(row):
            if board[i] == col:
                return False
            if abs(board[i] - col) == abs(i - row):
                return False
        return True

    def solve(row):
        if row == n:
            return True

        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                if solve(row + 1):
                    return True
                board[row] = -1
        return False

    if solve(0):
        for row in range(n):
            for col in range(n):
                if board[row] == col:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
    else:
        print("No solution found")


n = 4
solve_n_queens(n)
