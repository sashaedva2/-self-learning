# -*- coding: utf-8 -*-

import simple_draw as sd


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции
# def triangle(point, angle=0, length=100):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
#     v2.draw()
#     v1 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
#     v1.draw()
#
#
# def square(point, angle=0, length=100):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
#     v2.draw()
#     v1 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 270, length=length, width=3)
#     v2.draw()
#
#
# def pentagon(point, angle=0, length=100):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
#     v2.draw()
#     v1 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 216, length=length, width=3)
#     v2.draw()
#     v1 = sd.get_vector(start_point=v2.end_point, angle=angle + 288, length=length, width=3)
#     v1.draw()
#
#
# def hexagon(point, angle=0, length=100):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
#     v2.draw()
#     v1 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 180, length=length, width=3)
#     v2.draw()
#     v1 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 300, length=length, width=3)
#     v2.draw()
#
#
# point = sd.get_point(100, 100)
# triangle(point)
#
# point = sd.get_point(400, 400)
# square(point, 0, 80)
#
# point = sd.get_point(200, 400)
# pentagon(point)
#
# point = sd.get_point(400, 200)
# hexagon(point)


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


point = sd.get_point(100, 100)
triangle(point)

point = sd.get_point(400, 400)
square(point, 0, 80)

point = sd.get_point(200, 400)
pentagon(point)

point = sd.get_point(400, 200)
hexagon(point)

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
