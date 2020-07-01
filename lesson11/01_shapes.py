# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.
def draw_figure(start_point, angle, length):
    v = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
    v.draw()
    return v.end_point


def triangle(point, angle=0, length=100):
    start = draw_figure(start_point=point, angle=angle, length=length)
    for i in range(1, 3):
        start = draw_figure(start_point=start, angle=angle + i * 120, length=length)


def square(point, angle=0, length=100):
    start = draw_figure(start_point=point, angle=angle, length=length)
    for i in range(1, 4):
        start = draw_figure(start_point=start, angle=angle + i * 90, length=length)


def pentagon(point, angle=0, length=100):
    start = draw_figure(start_point=point, angle=angle, length=length)
    for i in range(1, 5):
        start = draw_figure(start_point=start, angle=angle + i * 72, length=length)


def hexagon(point, angle=0, length=100):
    start = draw_figure(start_point=point, angle=angle, length=length)
    for i in range(1, 6):
        start = draw_figure(start_point=start, angle=angle + i * 60, length=length)


def get_polygon(n):
    if n == 3:
        return triangle
    elif n==4:
        return square
    elif n== 5:
        return pentagon
    elif n== 6:
        return hexagon
    else:
        raise Exception('Программа рисует только от теругольника до 6-угольника')


draw_triangle = get_polygon(n=4)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)

sd.pause()
