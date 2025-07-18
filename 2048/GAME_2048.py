import random

def init_board():
    """Создаём пустое поле 4x4 и добавляем 2 стартовые клетки."""
    board = [[0] * 4 for _ in range(4)]
    add_random_tile(board)
    add_random_tile(board)
    return board

def add_random_tile(board):
    """Добавляет 2 или 4 в случайную пустую клетку."""
    empty_cells = [
        (i, j) 
        for i in range(4) 
        for j in range(4) 
        if board[i][j] == 0
    ]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = random.choice([2, 4])


def print_board(board):
    for row in board:
        print(" ".join(f"{num:4}" if num != 0 else "   ." for num in row))
    print()




def move_left(board):
    """Сдвигаем все клетки влево и объединяем одинаковые."""
    for row in board:
        # Удаляем нули: [2, 0, 2, 4] → [2, 2, 4]
        non_zero = [num for num in row if num != 0]
        
        # Объединяем соседей: [2, 2, 4] → [4, 0, 4]
        merged = []
        skip = False
        for i in range(len(non_zero)):
            if skip:
                skip = False
                continue
            if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
                merged.append(non_zero[i] * 2)
                skip = True
            else:
                merged.append(non_zero[i])
        merged += [0] * (4 - len(merged))
        
        # Обновляем строку
        row[:] = merged


def handle_input(board, cmd):
    """Обрабатываем WASD для сдвига."""
    move = input("WASD для движения (Q для выхода): ").upper()
    if move == "A":
        move_left(board)
    elif move == "D":
        # Сдвиг вправо (зеркально left)
        for row in board:
            row.reverse()
        move_left(board)
        for row in board:
            row.reverse()
    elif move == "W":
        # Сдвиг вверх (транспонируем матрицу)
        board[:] = [list(row) for row in zip(*board)]
        move_left(board)
        board[:] = [list(row) for row in zip(*board)]
    elif move == "S":
        # Сдвиг вниз
        board[:] = [list(row) for row in zip(*board)]
        for row in board:
            row.reverse()
        move_left(board)
        for row in board:
            row.reverse()
        board[:] = [list(row) for row in zip(*board)]
    elif move == "Q":
        return False
    return True


def check_win(board):
    """Проверяем, есть ли на поле 2048."""
    return any(2048 in row for row in board)

def check_lose(board):
    """Проверяем, остались ли возможные ходы."""
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if j + 1 < 4 and board[i][j] == board[i][j + 1]:
                return False
            if i + 1 < 4 and board[i][j] == board[i + 1][j]:
                return False
    return True


def main():
    """Главный игровой цикл."""
    board = init_board()
    while True:
        print_board(board)
        
        # Проверка победы/проигрыша
        if check_win(board):
            print("Поздравляю! Вы достигли 2048! 🎉")
            break
        if check_lose(board):
            print("Игра окончена. Не осталось ходов. 💀")
            break
            
        # Обработка ввода
        cmd = input("WASD (движение), Q (выход): ").upper()
        if cmd == "Q":
            break
        elif cmd in ("W", "A", "S", "D"):
            handle_input(board, cmd)
            add_random_tile(board)
        else:
            print("Неверная команда! Используйте WASD или Q")


if __name__ == "__main__":
    main()
