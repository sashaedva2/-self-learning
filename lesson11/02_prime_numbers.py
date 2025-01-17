# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:
    def __init__(self, n):
        self.i, self.n = 1, n
        self.prime_numbers = []

    def __iter__(self):
        # обнуляем счетчик перед циклом
        self.i = 1
        # возвращаем ссылку на себя - я буду итератором!
        return self

    def __next__(self):
        # а этот метод возвращает значения по требованию python
        self.i += 1
        for prime in self.prime_numbers:
            if self.i % prime == 0:
                return self.__next__()
        else:
            if self.i > self.n:
                raise StopIteration()
            self.prime_numbers.append(self.i)
            return self.i


# prime_number_iterator = PrimeNumbers(n=10)
# for number in prime_number_iterator:
#     print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    i = 1
    prime_numbers = []
    while True:
        i += 1
        for prime in prime_numbers:
            if i % prime == 0:
                break
        else:
            if i > n:
                return
            prime_numbers.append(i)
            yield i, 'Счастливое: {0} , Полидром: {1}'.format(happy_number(i),
                                                              polidrom(i))


def happy_number(n):
    c = list(str(n))
    s = 0
    if len(c) > 1:
        while len(c) > 1:
            s += int(c[0])
            s -= int(c[-1])
            del c[0], c[-1]
    else:
        return False
    if s == 0:
        return True
    else:
        return False


def polidrom(n):
    c = list(str(n))
    a = list(str(n))
    a.reverse()
    if c == a:
        return True
    else:
        return False


for number in prime_numbers_generator(n=1000):
    print(number)
# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
