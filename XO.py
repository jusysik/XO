# Рисуем игровое поле
def draw_board(board):
    for i in range(3):
        print(' │ '.join(board[i]))
        if i < 2:
            print('─'*9)


# Проверяем победителя
def check_winner(board, player):
    # По горизонтали
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    # По вертикали
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    # По диагоналям
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


# Реализация ходов игроков
def make_move(board, player, row, col):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    else:
        return False


# Инициализация игрового поля
board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'

# Игра
while True:
    # Отображение игрового поля
    draw_board(board)

    # Запрос хода у текущего игрока
    row = int(input('Введите номер строки (0-2): '))
    col = int(input('Введите номер столбца (0-2): '))

    # Попытка осуществить ход
    if make_move(board, current_player, row, col):
        # Проверка победителя
        if check_winner(board, current_player):
            draw_board(board)
            print('Игрок', current_player, 'победил!')
            break
        # Проверка ничьей
        elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            draw_board(board)
            print('Ничья!')
            break

        # Смена игрока
        current_player = 'O' if current_player == 'X' else 'X'
    else:
        print('Данная позиция уже занята, выберете другую.')