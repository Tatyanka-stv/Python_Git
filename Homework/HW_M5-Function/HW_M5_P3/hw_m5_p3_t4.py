import random

def create_board():
    board = [[0] * 4 for _ in range(4)]
    numbers = list(range(1, 16))
    random.shuffle(numbers)
    for i in range(4):
        for j in range(4):
            if i == 3 and j == 3:
                board[i][j] = 0  # це буде порожня комірка
            else:
                board[i][j] = numbers.pop()
    return board

def print_board(board):
    for row in board:
        print(" ".join(map(lambda x: f"{x:2}" if x else "  ", row)))


def find_empty_cell(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return (i, j)


def move_cell_with_number(board, direction):
    i, j = find_empty_cell(board)
    if direction == 'left' or direction == 'l':
        if j < 3:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
    elif direction == 'right' or direction == 'r':
        if j > 0:
            board[i][j], board[i][j - 1] = board[i][j - 1], board[i][j]
    elif direction == 'up' or direction == 'u':
        if i < 3:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
    elif direction == 'down' or direction == 'd':
        if i > 0:
            board[i][j], board[i - 1][j] = board[i - 1][j], board[i][j]


def is_win(board):
    winning_board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    return board == winning_board


def play_game():
    board = create_board()
    while True:
        print_board(board)
        if is_win(board):
            print("Ви виграли!")
            break
        move_direction = input('Вкажіть як рухати плитку з цифрою (ліворуч ''"''left''"'', праворуч ''"''right''"'', вгору ''"''up''"'', вниз ''"''down''"'' або ''"''q''"'' для виходу: ')
        if move_direction == 'q':
            print('Гра закінчена.')
            break
        if move_direction in ['left', 'l', 'right', 'r', 'up', 'u', 'down', 'd']:
            move_cell_with_number(board, move_direction)
        else:
            print('Невірний напрям руху плитки. Спробуйте ще раз.')


play_game()