# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+ё
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import zipfile


class Char_stat:
    total = 0

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self._collect_for_line(line=line[:-1])

    def _collect_for_line(self, line):
        for char in line:
            if char in self.stat:
                self.stat[char] += 1
            else:
                self.stat[char] = 1
            self.total += 1

    def table(self):
        print('+---------+----------+')
        print('|  буква  | частота  |')
        print('+---------+----------+')
        self.sort_stat()
        print('+---------+----------+')
        print('|  итого  | {0:7d}  |'.format(self.total))
        print('+---------+----------+')

    def sort_stat(self):
        for char, stat in self.stat.items():
            print('|    {0}    |   {1:6d} |'.format(char, stat))


class Char_stat_sort1(Char_stat):
    def sort_stat(self):
        list_d = list(self.stat.items())
        list_d.sort(key=lambda i: i[1])
        for i in list_d:
            print('|    {0}    |   {1:6d} |'.format(i[0], i[1]))


class Char_stat_sort2(Char_stat):
    def sort_stat(self):
        list_d = list(self.stat.keys())
        list_d.sort()
        for i in list_d:
            print('|    {0}    |   {1:6d} |'.format(i, self.stat[i]))


class Char_stat_sort3(Char_stat):
    def sort_stat(self):
        list_d = list(self.stat.keys())
        list_d.sort(reverse=True)
        for i in list_d:
            print('|    {0}    |   {1:6d} |'.format(i, self.stat[i]))


chatterer = Char_stat_sort3(file_name='voyna-i-mir.txt.zip')
chatterer.collect()
chatterer.table()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
