# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class Log_parser:

    def __init__(self, file_inp, file_out):
        self.file_inp = file_inp
        self.file_out = file_out
        self.stat = 0
        self.flag = ''
        self.stat_write = ''

    def read_file(self):
        self.file_output = open(self.file_out, 'w', encoding='utf-8')
        with open(self.file_inp, 'r', encoding='utf-8') as file_inp:
            for line in file_inp:
                self._collect_for_line(line=line[:-1])
        self.file_output.close()

    def _collect_for_line(self, line):
        if self.flag != line[16]:
            self.write_log()
            self.stat = 0
            self.flag = line[16]
            self.stat_write = line[:17]

        if 'NOK' in line:
            self.stat += 1

    def write_log(self):
        if self.stat_write > '':
            self.file_output.write('{0}] {1:3d}\n'.format(self.stat_write, self.stat))


log_parser = Log_parser(file_inp='events.txt', file_out='log.txt')
log_parser.read_file()
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
