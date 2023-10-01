
example_array = [[" ", 0   , 1   ,   2],
                 [0  , "-" , "-" , "-"],
                 [1  , "-" , "-" , "-"],
                 [2  , "-" , "-" , "-"]]

def print_maps():
    print(*example_array[0])
    print(*example_array[1])
    print(*example_array[2])
    print(*example_array[3])

# Сделать ход в ячейку
def step_maps(step_x, step_y, symbol):

    if example_array[step_x+1][step_y+1]=="-":
        example_array[step_x+1][step_y+1]=symbol
        return "Ok"
    else:
        print("Будьте внимательнее, эта ячейка уже заполненат!")
        return "-"
    # else:
    #     print("Будьте внимательнее, эта ячейка уже заполнена или не существует!")

# Получить текущий результат игры
def get_result():
    win = ""
    # victories = [[example_array[1][1], example_array[1][2], example_array[1][3]],
    #              [example_array[2][1], example_array[2][2], example_array[2][3]],
    #              [example_array[3][1], example_array[3][2], example_array[3][3]],
    #              [example_array[1][1], example_array[2][2], example_array[1][3]],
    #              [example_array[2][1], example_array[2][2], example_array[2][3]],
    #              [example_array[3][1], example_array[3][2], example_array[3][3]],
    #              [example_array[1][1], example_array[2][2], example_array[3][3]],
    #              [example_array[3][1], example_array[2][2], example_array[1][3]]]
    if (example_array[1][1] == "X" and example_array[1][2] == "X" and example_array[1][3] == "X"):
        win = "X"
        print("ura")
    if (example_array[2][1] == "X" and example_array[2][2] == "X" and example_array[2][3] == "X"):
        win = "X"
        print("ura")
    if (example_array[3][1] == "X" and example_array[3][2] == "X" and example_array[3][3] == "X"):
        win = "X"
        print("ura")
    if (example_array[1][1] == "X" and example_array[2][1] == "X" and example_array[3][1] == "X"):
        win = "X"
        print("ura")
    if (example_array[1][2] == "X" and example_array[2][2] == "X" and example_array[3][2] == "X"):
        win = "X"
        print("ura")
    if (example_array[1][3] == "X" and example_array[2][3] == "X" and example_array[3][3] == "X"):
        win = "X"
        print("ura")
    if (example_array[1][1] == "X" and example_array[2][2] == "X" and example_array[3][3] == "X"):
        win = "X"
        print("ura")
    if (example_array[3][1] == "X" and example_array[2][2] == "X" and example_array[1][3] == "X"):
        win = "X"
        print("ura")

    if (example_array[1][1] == "O" and example_array[1][2] == "O" and example_array[1][3] == "O"):
        win = "O"
        print("ura")
    if (example_array[2][1] == "O" and example_array[2][2] == "O" and example_array[2][3] == "O"):
        win = "O"
        print("ura")
    if (example_array[3][1] == "O" and example_array[3][2] == "O" and example_array[3][3] == "O"):
        win = "O"
        print("ura")
    if (example_array[1][1] == "O" and example_array[2][1] == "O" and example_array[3][1] == "O"):
        win = "O"
        print("ura")
    if (example_array[1][2] == "O" and example_array[2][2] == "O" and example_array[3][2] == "O"):
        win = "O"
        print("ura")
    if (example_array[1][3] == "O" and example_array[2][3] == "O" and example_array[3][3] == "O"):
        win = "O"
        print("ura")
    if (example_array[1][1] == "O" and example_array[2][2] == "O" and example_array[3][3] == "O"):
        win = "O"
        print("ura")
    if (example_array[3][1] == "O" and example_array[2][2] == "O" and example_array[1][3] == "O"):
        win = "O"
        print("ura")



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
        step_x = int(input("Игрок №1, Вы играете X, Выберете номер по горизонтали: "))
        while step_x<0 or step_x>2:
            print("Будьте внимательнее, эта ячейка не существует!" )
            print_maps()
            step_x = int(input("Игрок №1, Вы играете X, Выберете номер по горизонтали: "))

        step_y = int(input("Игрок №1, Вы играете X, Выберете номер по вертикали: "))
        print(step_x)
        while step_y < 0 or step_y > 2:
            print("Будьте внимательнее, эта ячейка не существует!")
            print_maps()
            step_y = int(input("Игрок №1, Вы играете X, Выберете номер по вертикали: "))
    else:
        symbol = "O"
        step_x = int(input("Игрок №2, Вы играете O, Выберете номер по горизонтали: "))
        step_y = int(input("Игрок №2, Вы играете O, Выберете номер по вертикали: "))

    if step_maps(step_x, step_y, symbol) == "Ok":  # делаем ход в указанную ячейку

        win = get_result()  # определим победителя

        if win != "":
            game_over = True
        else:
            game_over = False

        player1 = not (player1)


print(f'Победил {win}')
# # Вывод:
# [-1, 0, 0, 1]
# [2, 3, 5, 8]
# 1