from random import randint

global _number
_number = list()


def guess_the_number():
    """Загадывание числа"""
    version_num = list(range(10))
    num = randint(1, 9)
    _number.append(version_num[num])
    del version_num[num]
    for i in range(1, 4):
        num = randint(0, 9 - i)
        _number.append(version_num[num])
        del version_num[num]
    print(_number)


def check_the_number(answer):
    """Проверка числа и вывод результата в виде словаря"""
    result = [['bulls', 0], ['cows', 0]]
    i = 1
    for num in _number:
        j = 1
        for char in answer:
            if char == str(num):
                if i == j:
                    result[0][1] += 1
                else:
                    result[1][1] += 1
            j += 1
        i += 1

    return dict(result)
