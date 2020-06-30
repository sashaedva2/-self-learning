# -*- coding: utf-8 -*-
from random import randint


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
def one_day():
    try:
        dice1 = randint(1, 7)
        dice2 = randint(1, 13)
        if dice2==1:
            raise IamGodError('Я бог')
        elif dice2==2:
            raise DrunkError('Я напился')
        elif dice2==3:
            raise CarCrashError('Автомобильная авария')
        elif dice2==4:
            raise GluttonyError('Умер от еды')
        elif dice2==5:
            raise DepressionError('Депресссия')
        elif dice2==6:
            raise SuicideError('Суицид')
        return dice1
    except IamGodError:
        print('Все будут так говорить если попадут в временную петлю')
    except DrunkError:
        print('Алкоголь зло')
    except CarCrashError:
        print('Дороги скользкие, осторожней')
    except GluttonyError:
        print('Еда конечно хорошо, но в меру')
    except DepressionError:
        print('Надо что-то делать, сменить род деятельности')
    except SuicideError:
        print('Не поможет смерть от временой петли')
    return 0


ENLIGHTENMENT_CARMA_LEVEL = 777
Day = 0
Karma = 0
while True:
    Day += 1
    print(f'День {Day}')
    Karma += one_day()
    print(f'Карма {Karma}')
    if Karma >= ENLIGHTENMENT_CARMA_LEVEL:
        print('Петля времени оборвана')
        break
