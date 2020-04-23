# -*- coding: utf-8 -*-
import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

def draw_figure(start_point, angle, length, color=sd.COLOR_RED):
    v = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
    v.draw(color=color)
    return v.end_point


def triangle(point, angle=0, length=100, color=sd.COLOR_RED):
    start = draw_figure(start_point=point, angle=angle, length=length, color=color)
    for i in range(1, 3):
        start = draw_figure(start_point=start, angle=angle + i * 120, length=length, color=color)


def square(point, angle=0, length=100, color=sd.COLOR_RED):
    start = draw_figure(start_point=point, angle=angle, length=length, color=color)
    for i in range(1, 4):
        start = draw_figure(start_point=start, angle=angle + i * 90, length=length, color=color)


def pentagon(point, angle=0, length=100, color=sd.COLOR_RED):
    start = draw_figure(start_point=point, angle=angle, length=length, color=color)
    for i in range(1, 5):
        start = draw_figure(start_point=start, angle=angle + i * 72, length=length, color=color)


def hexagon(point, angle=0, length=100, color=sd.COLOR_RED):
    start = draw_figure(start_point=point, angle=angle, length=length, color=color)
    for i in range(1, 6):
        start = draw_figure(start_point=start, angle=angle + i * 60, length=length, color=color)


print('Возможные цвета:')
print('\t 0:RED\n\t 1:ORANGE\n\t 2:YELLOW\n\t 3:GREEN\n\t 4:CYAN')
print('\t 5:BLUE\n\t 6:PURPLE')
number_color = int(input('Введите номер желаемого цвета  '))
while not(number_color in range(7)):
    print('ВВедён некоректный номер!')
    number_color = int(input('Введите номер желаемого цвета  '))
point = sd.get_point(100, 100)
triangle(point, color=rainbow_colors[number_color])

point = sd.get_point(400, 400)
square(point, color=rainbow_colors[number_color])

point = sd.get_point(200, 400)
pentagon(point, color=rainbow_colors[number_color])

point = sd.get_point(400, 200)
hexagon(point, color=rainbow_colors[number_color])
sd.pause()
