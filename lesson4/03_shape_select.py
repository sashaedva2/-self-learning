# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

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


print('Возможные фигуры:')
print('\t 0:Треугольник\n\t 1:Квадрат\n\t 2:Пятиугольник\n\t 3:Шестиугольник')
number_figure = int(input('Введите номер желаемой фигуры  '))
while not(number_figure in range(4)):
    print('ВВедён некоректный номер!')
    number_figure = int(input('Введите номер желаемой фигуры  '))
sd.resolution = (600, 600)
point = sd.get_point(300, 300)
if number_figure == 0:
    triangle(point)
elif number_figure == 1:
    square(point)
elif number_figure == 2:
    pentagon(point)
elif number_figure == 3:
    hexagon(point)
sd.pause()
