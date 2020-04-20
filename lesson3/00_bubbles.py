# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(500, 500)
radius = 50
for _ in range(5):
    radius += 5
    sd.circle(point, radius, width=3)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг



def bubble(point, step):
    radius = 20
    for _ in range(5):
        radius += step
        sd.circle(point, radius, width=3)

point = sd.get_point(200, 200)
bubble(point, 10)

# Нарисовать 10 пузырьков в ряд
for x in range(100, 1001, 100):
    point = sd.get_point(x, 300)
    bubble(point, 5)


# Нарисовать три ряда по 10 пузырьков
 for y in range(200,401,100):
     for x in range(100, 1001, 100):
         point = sd.get_point(x, y)
         bubble(point, 5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    bubble(point, 5)

sd.pause()
