# Початкова дошка
board = [" " for _ in range(9)]

# Функція для виведення  дошки гри
def print_board(board):
    print(" | ".join(board[:3]))
    print("---------")
    print(" | ".join(board[3:6]))
    print("---------")
    print(" | ".join(board[6:9]))

# Функція для вводу ходу гравця
def player_move(board, player):
    valid_move = False
    while not valid_move:
        move = input('Гравець '+str(player) + ', введіть номер клітинки (1-9): ')
        try:
            move = int(move)
            if (move >=1 and move <= 9) and board[move - 1] == " ":
                valid_move = True
            else:
                print("Недійсний хід. Спробуйте ще раз.")
        except ValueError:
            print("Недійсний ввід. Введіть номер клітинки (1-9).")
    board[move - 1] = player

# Функція для перевірки переможця
def check_winner(board, player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Основний цикл гри
current_player = "X"
print_board(board)

for _ in range(9):  
    player_move(board, current_player)
    print_board(board)
    if check_winner(board, current_player):
        print('Гравець '+str(current_player)+' переміг!')
        break
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
else:
    print("Нічия!")