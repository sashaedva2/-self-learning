# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:
    num = 1

    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if other.num == 2:
            return Storm(part1=self, part2=other)
        elif other.num == 3:
            return Steam(part1=self, part2=other)
        elif other.num == 4:
            return Dirt(part1=self, part2=other)
        elif other.num == 5:
            return Fish(part1=self, part2=other)
        else:
            return None


class Air:
    num = 2

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if other.num == 1:
            return Storm(part1=self, part2=other)
        elif other.num == 3:
            return Lightning(part1=self, part2=other)
        elif other.num == 4:
            return Dust(part1=self, part2=other)
        elif other.num == 5:
            return Birds(part1=self, part2=other)
        else:
            return None


class Fire:
    num = 3

    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if other.num == 1:
            return Steam(part1=self, part2=other)
        elif other.num == 2:
            return Lightning(part1=self, part2=other)
        elif other.num == 4:
            return Lava(part1=self, part2=other)
        elif other.num == 5:
            return Dragon(part1=self, part2=other)
        else:
            return None


class Earth:
    num = 4

    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if other.num == 1:
            return Dirt(part1=self, part2=other)
        elif other.num == 2:
            return Dust(part1=self, part2=other)
        elif other.num == 3:
            return Lava(part1=self, part2=other)
        elif other.num == 5:
            return Golem(part1=self, part2=other)
        else:
            return None


class Live:
    num = 5

    def __str__(self):
        return 'Жизнь'

    def __add__(self, other):
        if other.num == 1:
            return Fish(part1=self, part2=other)
        elif other.num == 2:
            return Birds(part1=self, part2=other)
        elif other.num == 3:
            return Dragon(part1=self, part2=other)
        elif other.num == 4:
            return Golem(part1=self, part2=other)
        else:
            return None


class Storm:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Шторм'


class Steam:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Пар'


class Dirt:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Грязь'


class Lightning:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Молния'


class Dust:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Пыль '


class Lava:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Лава'


class Fish:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Рыбы'


class Birds:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Птицы'


class Dragon:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Дракон'


class Golem:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Голем'


print(Water(), ' + ', Live(), ' = ', Water() + Live())
print(Live(), ' + ', Air(), ' = ', Live() + Air())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
