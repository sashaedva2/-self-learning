# -*- coding: utf-8 -*-

import simple_draw as sd
from random import randint

colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
          sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE, sd.COLOR_WHITE)
# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall
from snowfall_engine import create_snowdrops, draw_snowdrop_with_color, move_snowdrops, number_to_bottom_of_screen, \
    del_snowdrop
sd.resolution = (600, 800)
N = 10
# создать_снежинки(N)
create_snowdrops(N)
while True:
    # sd.start_drawing()
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    draw_snowdrop_with_color(color=sd.background_color)
    #  сдвинуть_снежинки()
    move_snowdrops()
    #  нарисовать_снежинки_цветом(color)
    draw_snowdrop_with_color(color=colors[randint(0, 7)])
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки()
    #       создать_снежинки(count)
    if number_to_bottom_of_screen():
        del_snowdrop()
        create_snowdrops(randint(1, 2))
    # sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
