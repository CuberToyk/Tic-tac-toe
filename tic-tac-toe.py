def print_board(board):
    """
    Функционал печати поля.
    Отображает текущее состояние игрового поля в консоли.
    """
    print("\n   | 0 | 1 | 2 |")
    print("----------------")
    for i, row in enumerate(board):
        print(f" {i} | {' | '.join(row)} |")
        print("----------------")


def check_winner(board):
    """
    Функция проверки завершенности игры.
    Проверяет текущее состояние игрового поля и определяет, завершилась ли игра.
    Возвращает:
        'X' - победили крестики
        'O' - победили нолики
        'draw' - ничья
        None - игра продолжается
    """
    # Проверка строк
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    # Проверка столбцов
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    # Проверка на ничью
    if all(cell != ' ' for row in board for cell in row):
        return 'draw'

    return None


def get_player_move(board, current_player):
    """
    Проверка корректности ввода.
    Получает и проверяет корректность ввода пользователем координат для хода.
    """
    while True:
        try:
            move = input(f"\nИгрок {current_player}, введите ваш ход (строка столбец, например '0 1'): ")
            row, col = map(int, move.split())

            # Проверка диапазона координат
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Ошибка: координаты должны быть от 0 до 2!")
                continue

            # Проверка занятости клетки
            if board[row][col] != ' ':
                print("Ошибка: эта клетка уже занята!")
                continue

            return row, col

        except ValueError:
            print("Ошибка: введите два числа через пробел (например '0 1')!")
        except KeyboardInterrupt:
            raise


def play_game():
    """
    Основная функция игры.
    Реализует пользовательский интерфейс для взаимодействия с игрой.
    """
    # Инициализация игрового поля
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print("=" * 50)
    print("       ДОБРО ПОЖАЛОВАТЬ В КРЕСТИКИ-НОЛИКИ!")
    print("=" * 50)
    print("\nПравила:")
    print("- Игроки по очереди ставят X и O на поле 3x3")
    print("- Для хода введите два числа: номер строки и номер столбца")
    print("- Например: '0 1' - первая строка, второй столбец")
    print("- Побеждает тот, кто первым выстроит 3 своих символа в ряд")
    print("=" * 50)

    print_board(board)

    while True:
        try:
            # Получаем ход от текущего игрока
            row, col = get_player_move(board, current_player)

            # Выполняем ход
            board[row][col] = current_player
            print_board(board)

            # Проверяем состояние игры
            result = check_winner(board)

            if result == 'X':
                print("\nПоздравляем! Игрок X победил!")
                break
            elif result == 'O':
                print("\nПоздравляем! Игрок O победил!")
                break
            elif result == 'draw':
                print("\nНичья! Поле полностью заполнено!")
                break

            # Передаем ход следующему игроку
            current_player = 'O' if current_player == 'X' else 'X'

        except KeyboardInterrupt:
            print("\n\nИгра прервана. До свидания!")
            break


def main():
    """
    Главная функция с меню игры.
    """
    while True:
        print("\n" + "=" * 50)
        print("             КРЕСТИКИ-НОЛИКИ")
        print("=" * 50)
        print("1. Начать новую игру")
        print("2. Правила игры")
        print("3. Выход")

        choice = input("\nВыберите действие (1-3): ").strip()

        if choice == '1':
            play_game()

            # Предложение сыграть еще раз
            while True:
                again = input("\nХотите сыграть еще раз? (да/нет): ").lower().strip()
                if again in ['да', 'д', 'yes', 'y']:
                    break
                elif again in ['нет', 'н', 'no', 'n']:
                    print("Спасибо за игру! До свидания!")
                    return
                else:
                    print("Пожалуйста, введите 'да' или 'нет'")

        elif choice == '2':
            print("\n" + "=" * 50)
            print("                ПРАВИЛА ИГРЫ")
            print("=" * 50)
            print("1. Игровое поле 3x3 клетки")
            print("2. Игроки ходят по очереди")
            print("3. Первый игрок ставит X, второй - O")
            print("4. Для хода введите два числа через пробел:")
            print("   - Первое число: номер строки (0, 1, 2)")
            print("   - Второе число: номер столбца (0, 1, 2)")
            print("5. Побеждает тот, кто первым соберет линию")
            print("   из 3 своих символов (по горизонтали,")
            print("   вертикали или диагонали)")
            print("6. Если все клетки заполнены, но победителя")
            print("   нет - объявляется ничья")
            input("\nНажмите Enter чтобы продолжить...")

        elif choice == '3':
            print("До свидания!")
            break
        else:
            print("Неверный выбор! Пожалуйста, введите 1, 2 или 3.")


# Запуск игры
if __name__ == "__main__":
    main()