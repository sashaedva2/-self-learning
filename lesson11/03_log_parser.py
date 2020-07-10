# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

# class Log_parser:
#     def __init__(self, file_inp):
#         self.file_inp = file_inp
#         self.stat = 0
#         self.flag = ''
#         self.stat_write = ''
#
#     def __iter__(self):
#         # обнуляем счетчик перед циклом
#         self.stat = 0
#         self.flag = ''
#         self.stat_write = ''
#         self.file = open(self.file_inp, 'r', encoding='utf-8')
#         # возвращаем ссылку на себя - я буду итератором!
#         return self
#
#     def __next__(self):
#         # а этот метод возвращает значения по требованию python
#         for line in self.file:
#             if self.flag != line[16]:
#                 self.flag = line[16]
#                 return self.stat_write, self.stat
#                 self.stat = 0
#                 self.stat_write = line[:17]
#
#
#             if 'NOK' in line:
#                 self.stat += 1
#                 return self.__next__()
#         self.file.close()
#         raise StopIteration()

def Log_parser(file_inp):
    with open(file_inp, 'r', encoding='utf-8') as file_inp:
        stat = 0
        flag = ''
        stat_write = ''
        for line in file_inp:
            if flag != line[16]:
                yield stat_write, stat
                stat = 0
                flag = line[16]
                stat_write = line[:17]
            if 'NOK' in line:
                stat += 1


grouped_events = Log_parser(file_inp='events.txt')
for group_time, event_count in grouped_events:
    print(f'{group_time}] {event_count}')
