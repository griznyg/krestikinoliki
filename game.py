from chrushTest import print_maps, step_maps, crush_test, get_result
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

# Основная программа
game_over = False
player1 = True
while game_over == False:
    # 1. Показываем карту
    print_maps(maps)
    # 2. Спросим у играющего куда делать ход
    if player1 == True:
        symbol = "X"
        print("Ход крестиков")
    else:
        symbol = "O"
        print("Ход ноликов")
    step = crush_test(maps)

    step_maps(step, symbol, maps)  # делаем ход в указанную ячейку
    win = get_result(victories, maps)  # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

# Игра окончена. Покажем карту. Объявим победителя.
print_maps(maps)
print("Победил", win)
