board = [' '] * 9

def display():
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
        if i < 6:
            print("---------")


def check_winner(player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def heuristic(player):
    opponent = 'O' if player == 'X' else 'X'
    score = 0
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for line in wins:
        values = [board[i] for i in line]
        if opponent not in values:
            score += values.count(player)
    return score


def best_move():
    best_score = -1
    move = None

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = heuristic('O')
            if check_winner('O'):
                score += 100
            board[i] = ' '

            if score > best_score:
                best_score = score
                move = i
    return move


print("Tic-Tac-Toe")
display()

for turn in range(9):
    if turn % 2 == 0:
        pos = int(input("Player X, enter position (0-8): "))

        if pos < 0 or pos > 8 or board[pos] != ' ':
            print("Invalid position!")
            continue

        board[pos] = 'X'
        if check_winner('X'):
            display()
            print("Player X wins!")
            break
    else:
        pos = best_move()
        board[pos] = 'O'
        print("Computer O chooses:", pos)

        if check_winner('O'):
            display()
            print("Computer O wins!")
            break

    display()
else:
    print("Match Draw!")
