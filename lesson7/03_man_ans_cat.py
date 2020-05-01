# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.
from termcolor import cprint


class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.catfood >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.catfood -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        cprint('{} поспал'.format(self.name), color='green')
        self.fullness -= 10

    def work(self):
        cprint('{} Подрал обои'.format(self.name), color='red')
        self.house.dirt += 5
        self.fullness -= 10

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Забрали в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 3)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.sleep()


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')
            self.fullness -= 3
    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def play(self):
        cprint('{} Прокрастинировал целый день'.format(self.name), color='green')
        self.fullness -= 10

    def cleaning(self):
        cprint('{} Убирается'.format(self.name), color='blue')
        self.house.dirt -= 100
        self.fullness -= 20
        self.eat()

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 80
            self.house.food += 50
            self.house.catfood += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 3)
        if self.fullness < 20:
            self.eat()
        elif self.house.dirt >= 100:
            self.cleaning()
        elif self.house.money < 80:
            self.work()
        elif (self.house.food < 10) or (self.house.catfood < 10):
            self.shopping()

        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play()


class House:

    def __init__(self):
        self.food = 50
        self.money = 10
        self.catfood = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, кашачего корма осталось {}, кол-во грязи {}'.format(
            self.food, self.money, self.catfood, self.dirt)


Sasha = Man(name='Саша')
cats=[
    Cat('Люся'),
    Cat('Михаил'),
    Cat('Бакс'), ]

myhome = House()
Sasha.go_house(house=myhome)
for cat in cats:
    cat.go_to_the_house(house=myhome)
for day in range(1, 366):
    print('================ день {} =================='.format(day))
    Sasha.act()
    for cat in cats:
        cat.act()
    print('--- в конце дня ---')
    print(Sasha)
    for cat in cats:
        print(cat)
    print(myhome)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
