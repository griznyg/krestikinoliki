import sys

# Вывод карты на экран
def print_maps(maps):
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
def step_maps(step, symbol,maps):
    ind = maps.index(step)
    maps[ind] = symbol

# Проверка введенных данных
def crush_test(maps):
    it_is = False
    while it_is == False:
        step = input("Введите значение: ")
        try:
            step = int(step)
        except ValueError:
            print("Данные введены неверно! Число не является целым!")
        else:
            if 0 <= step <= 9 and step == maps[step - 1]:
                return step
                it_is = True
            else:
                print("Данные введены неверно! Номер поля не входит в диапазон от 1 до 9 или поле уже занято!")

# Получить текущий результат игры
def get_result(victories, maps):
    win = ""

    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"

    return win