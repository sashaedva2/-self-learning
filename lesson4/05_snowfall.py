# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20
list_snowfall = []
for _ in range(N):
    list_snowfall.append([sd.random_number(0, 600), 790])
list_ray = []
for _ in range(N):
    list_ray.append(sd.random_number(10, 60))

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()
sd.resolution = (800, 800)
while True:
    sd.start_drawing()
    for i in range(N):
        if list_snowfall[i][1] < 10:
            continue
        point = sd.get_point(*list_snowfall[i])
        sd.snowflake(center=point, length=list_ray[i])
        sd.snowflake(center=point, length=list_ray[i], color=sd.background_color)
        list_snowfall[i][1] -= 10 + sd.random_number(-10, 20)
        list_snowfall[i][0] += 10 + sd.random_number(-30, 10)
        point = sd.get_point(*list_snowfall[i])
        sd.snowflake(center=point, length=list_ray[i])
    sd.finish_drawing()
    sd.sleep(0.2)
    if sd.user_want_exit():
        break
sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
