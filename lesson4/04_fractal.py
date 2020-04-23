# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения
# sd.resolution = (800, 800)
#
#
# def draw_branches(point, angle, length):
#     if length < 2:
#         return
#     v1 = sd.get_vector(start_point=point, angle=angle + 30, length=length, width=1)
#     v1.draw()
#     next_point = v1.end_point
#     next_angle = angle + 30
#     next_length = length * .75
#     draw_branches(point=next_point, angle=next_angle, length=next_length)
#     v2 = sd.get_vector(start_point=point, angle=angle - 30, length=length, width=1)
#     v2.draw()
#     next_point = v2.end_point
#     next_angle = angle - 30
#     next_length = length * .75
#     draw_branches(point=next_point, angle=next_angle, length=next_length)
#
#
# root_point = sd.get_point(400, 30)
# draw_branches(point=root_point, angle=90, length=100)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg
sd.resolution = (800, 800)


def draw_branches_random(point, angle, length):
    if length < 4:
        return
    v1 = sd.get_vector(start_point=point, angle=angle + 30, length=length, width=1)
    v1.draw()
    next_point = v1.end_point
    next_angle = angle + 30 + .3 * sd.random_number(-40, 40)
    next_length = length * (.75 + 0.0075 * sd.random_number(-20, 20))
    draw_branches_random(point=next_point, angle=next_angle, length=next_length)
    v2 = sd.get_vector(start_point=point, angle=angle - 30, length=length, width=1)
    v2.draw()
    next_point = v2.end_point
    next_angle = angle - 30 + .3 * sd.random_number(-40, 40)
    next_length = length * (.75 + 0.0075 * sd.random_number(-20, 20))
    draw_branches_random(point=next_point, angle=next_angle, length=next_length)


root_point = sd.get_point(400, 30)
draw_branches_random(point=root_point, angle=85, length=150)
# Пригодятся функции
# sd.random_number()

sd.pause()
