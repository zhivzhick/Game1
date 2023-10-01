# Инициализация карты
maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]
# Инициализация победных линий
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]

def print_maps():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])

# Сделать ход в ячейку
def step_maps(step, symbol):

    if step in maps:
        ind = maps.index(step)
        maps[ind] = symbol
        return "Ok"
    else:
        print("Будьте внимательнее, эта ячейка уже заполнена или не существует!")

# Получить текущий результат игры
def get_result():
    win = ""

    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"

    return win

# Основная программа
print("Игра Крестики-нолики")
game_over = False
player1 = True

while game_over == False:

    # 1. Показываем карту
    print_maps()

    # 2. Спросим у играющего куда делать ход
    if player1 == True:
        symbol = "X"
        step = int(input("Игрок №1, Вы играете X, Выберете номер: "))
    else:
        symbol = "O"
        step = int(input("Игрок №2, Вы играете О, Выберете номер: "))

    if step_maps(step, symbol)=="Ok":  # делаем ход в указанную ячейку
        win = get_result()  # определим победителя
        if win != "":
            game_over = True
        else:
            game_over = False

        player1 = not (player1)

# Игра окончена. Покажем карту. Объявим победителя.
print(win)
print_maps()
print(f'Победил {win}')
