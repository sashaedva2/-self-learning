# -*- coding: utf-8 -*-
from random import randint

import simple_draw as sd

colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
          sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE, sd.COLOR_WHITE)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self):
        self.position = [randint(0, 600), 790]
        self.size = randint(10, 60)
        self.color = colors[randint(0, 7)]

    def move(self):
        """Сдвиг снежинок"""
        self.position[1] -= 10 + randint(-10, 20)
        self.position[0] += 10 + randint(-30, 10)

    def draw(self):
        point = sd.get_point(*self.position)
        sd.snowflake(center=point, length=self.size, color=self.color)

    def clear_previous_picture(self):
        point = sd.get_point(*self.position)
        sd.snowflake(center=point, length=self.size, color=sd.background_color)

    def can_fall(self):
        if self.position[1] < 10:
            self.clear_previous_picture()
            return True
        return False


flake = Snowflake()

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
