def is_valid(x, y, board):
    return 0 <= x < 8 and 0 <= y < 8 and board[x][y] == -1

def print_board(board):
    for row in board:
        print(row)

def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 7:
                return value
            else:
                print("Введене число повинно бути в діапазоні від 0 до 7.")
        except ValueError:
            print("Введіть ціле число від 0 до 7.")

def solve_knight_tour(board, x, y, move_count):
    if move_count == 64:  
        print_board(board)
        return True
  
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    
    next_moves = []

    for i in range(8):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if is_valid(next_x, next_y, board):
            next_moves.append((next_x, next_y))

        next_moves.sort(key=lambda move: len([(move[0] + dx[i], move[1] + dy[i])
        for i in range(8)
        if is_valid(move[0] + dx[i], move[1] + dy[i], board)]))

    for move in next_moves:
        board[move[0]][move[1]] = move_count
        if solve_knight_tour(board, move[0], move[1], move_count + 1):
            return True
        board[move[0]][move[1]] = -1

    return False

board = [[-1 for _ in range(8)] for _ in range(8)]


start_x = get_valid_input("Введіть початкову координату Х (0-7): ")
start_y = get_valid_input("Введіть початкову координату У (0-7): ")

board[start_x][start_y] = 0

if not solve_knight_tour(board, start_x, start_y, 1):
    print("Рішення не знайдено.")