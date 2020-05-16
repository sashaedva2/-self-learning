# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.food = 50
        self.money = 100
        # self.catfood = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, кол-во грязи {}'.format(
            self.food, self.money, self.dirt)
        # , кошачего корма осталось {} , self.catfood


class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happy = 100
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}, счастье {}'.format(
            self.name, self.fullness, self.happy)

    def go_house(self, house):
        self.house = house
        self.fullness -= 5
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')


class Husband(Man):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return super().__str__()

    def act(self):
        if (self.fullness <= 0) or (self.happy <= 0):
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 3)
        if self.fullness < 20:
            self.eat()
        elif self.house.money < 80:
            self.work()
        elif (self.happy < 15):
            self.gaming()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.gaming()
        if self.house.dirt > 90:
            self.happy -= 10

    def eat(self):
        if self.house.food >= 30:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 30
            self.house.food -= 30
            if self.fullness > 100:
                self.fullness = 100
        else:
            cprint('{} нет еды'.format(self.name), color='red')
            self.fullness -= 3

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def gaming(self):
        cprint('{} Играть целый день'.format(self.name), color='green')
        self.fullness -= 10
        self.happy += 20
        if self.happy > 100:
            self.happy = 100


class Wife(Man):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return super().__str__()

    def act(self):
        if (self.fullness <= 0) or (self.happy <= 0):
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 4)
        if self.fullness < 15:
            self.eat()
        elif (self.happy < 50) and (self.house.dirt > 90):
            self.clean_house()
        elif (self.happy < 20):
            self.buy_fur_coat()
        elif (self.house.food < 40):  # or (self.house.catfood < 10)
            self.shopping()
        elif dice == 1:
            self.shopping()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.clean_house()
        else:
            self.buy_fur_coat()
        if self.house.dirt > 90:
            self.happy -= 10

    def eat(self):
        if self.house.food >= 30:
            cprint('{} поела'.format(self.name), color='yellow')
            self.fullness += 30
            self.house.food -= 30
            if self.fullness > 100:
                self.fullness = 100
        else:
            cprint('{} нет еды'.format(self.name), color='red')
            self.fullness -= 3

    def buy_fur_coat(self):
        if self.house.money > 500:
            self.happy += 60
            self.house.money -= 350
            cprint('{} Купила шубу'.format(self.name), color='green')
            if self.happy > 100:
                self.happy = 100
        else:
            cprint('{} Поглядела шубу'.format(self.name), color='green')
            self.happy += 5

    def clean_house(self):
        cprint('{} Убирается'.format(self.name), color='blue')
        self.house.dirt -= 100
        if self.house.dirt < 0:
            self.house.dirt = 0
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 90:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 90
            self.house.food += 90
            # self.house.catfood += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')


######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов

class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Man):

    def __init__(self, name):
        super().__init__(name)
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(self.name, self.fullness)

    def act(self):
        if (self.fullness <= 0) or (self.happy <= 0):
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 2)
        if self.fullness < 15:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.eat()

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
            if self.fullness > 100:
                self.fullness = 100
        else:
            cprint('{} нет еды'.format(self.name), color='red')
            self.fullness -= 3

    def sleep(self):
        cprint('{} поспал'.format(self.name), color='green')
        self.fullness -= 5

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 5
        cprint('{} - появление в доме'.format(self.name), color='cyan')


children = [
    # Child('Люся'),
    Child('Михаил'),
    # Child('Бакс'),
    # Child('Кузя'),
    Child('Олег')]
home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
serge.go_house(house=home)
masha.go_house(house=home)
for child in children:
    child.go_to_the_house(house=home)
for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    home.dirt += 10
    serge.act()
    masha.act()
    for child in children:
        child.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    for child in children:
        cprint(child, color='cyan')
    cprint(home, color='cyan')

######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.

# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
