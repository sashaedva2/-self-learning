# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
def smile(point_x, point_y):
    radius = 50
    point = sd.get_point(point_x, point_y)
    sd.circle(point, radius, sd.COLOR_YELLOW)
    point = sd.get_point(point_x - 15, point_y + 20)
    sd.circle(point, 5, sd.COLOR_YELLOW)
    point = sd.get_point(point_x + 15, point_y + 20)
    sd.circle(point, 5, sd.COLOR_YELLOW)
    list_point = [sd.get_point(point_x - 25, point_y - 10), sd.get_point(point_x - 15, point_y - 20),
                  sd.get_point(point_x + 15, point_y - 20),
                  sd.get_point(point_x + 25, point_y - 10)]
    sd.lines(list_point, sd.COLOR_YELLOW, False)


for _ in range(20):
    smile(sd.random_number(50, 550), sd.random_number(50, 550))

sd.pause()
