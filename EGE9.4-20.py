def play(x, y, move):
    # Анализ текущей позиции после move ходов

    if x + y >= 77 and move == 3:
        return True
    if x + y < 77 and move == 3:
        return False
    if x + y >= 77:
        return False

    # Следующий ход
    # Для того, кто должен выиграть, должен сработать хотя бы один вариант
    # Для того, кто должен проиграть, должны сработать все варианты

    m1 = play(x + 1, y, move + 1)
    m2 = play(x * 2, y, move + 1)
    m3 = play(x, y + 1, move + 1)
    m4 = play(x, y * 2, move + 1)

    if move % 2 == 0:
        # Ходит Петя, он должен выиграть
        return m1 or m2 or m3 or m4
    else:
        # Ходит Ваня, он должен проиграть, не поддаваясь
        return m1 and m2 and m3 and m4


for s in range(1, 69 + 1):
    if play(7, s, 0):
        print(s)
