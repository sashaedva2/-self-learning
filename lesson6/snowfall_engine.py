from random import randint
import simple_draw as sd
colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
          sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE, sd.COLOR_WHITE)
global list_snowfall, list_ray, number
list_snowfall = list()
list_ray = list()
numbers = list()


def create_snowdrops(N):
    """Создание снежинок"""
    for _ in range(N):
        list_snowfall.append([randint(0, 600), 790])
    for _ in range(N):
        list_ray.append(randint(10, 60))


def draw_snowdrop_with_color(color):
    """Рисовать снежинки заданым цветом"""
    i = 0
    for snowfall in list_snowfall:
        point = sd.get_point(*snowfall)
        sd.snowflake(center=point, length=list_ray[i], color=color)
        i += 1


def move_snowdrops():
    """Сдвиг снежинок"""
    for snowfall in list_snowfall:
        snowfall[1] -= 10 + randint(-10, 20)
        snowfall[0] += 10 + randint(-30, 10)


def number_to_bottom_of_screen():
    """Список номеров упавших снежинок"""
    for i in range(len(list_snowfall)):
        if list_snowfall[i][1] < 0:
            numbers.append(i)
    if len(numbers) > 0:
        return True
    else:
        return False


def del_snowdrop():
    """Удаляет данные снежинки"""
    sd.clear_screen()
    draw_snowdrop_with_color(color=colors[randint(0, 7)])
    for num in numbers:
        del list_snowfall[num]
        del list_ray[num]
    numbers.clear()
