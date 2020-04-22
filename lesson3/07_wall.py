# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
sd.resolution = (600, 600)
for i in range(12):
    for j in range(6):
        if i % 2 == 0:
            start_point = sd.get_point(j * 100 + 50, i * 50)
            end_point = sd.get_point(j * 100 + 50, (i + 1) * 50)
        else:
            start_point = sd.get_point(j * 100, i * 50)
            end_point = sd.get_point(j * 100, (i + 1) * 50)
        sd.line(start_point, end_point, sd.COLOR_ORANGE)
    start_point = sd.get_point(0, i * 50)
    end_point = sd.get_point(600, i * 50)
    sd.line(start_point, end_point, sd.COLOR_ORANGE)

sd.pause()
