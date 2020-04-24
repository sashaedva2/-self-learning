# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1.room1 import folks as people1
from district.central_street.house1.room2 import folks as people2
from district.central_street.house2.room1 import folks as people3
from district.central_street.house2.room2 import folks as people4
from district.soviet_street.house1.room1 import folks as people11
from district.soviet_street.house1.room2 import folks as people12
from district.soviet_street.house2.room1 import folks as people13
from district.soviet_street.house2.room2 import folks as people14

dots = ', '
tags = [people1, people2, people3, people4, people11, people12, people13, people14]
people = []
for tag in tags:
    people.extend(tag)

pprint(dots.join(people))





