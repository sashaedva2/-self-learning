# -*- coding: utf-8 -*-
class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


class ValueageError(Exception):
    pass


# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
file_inp = 'registrations.txt'
file_good = 'registrations_good_log.txt'
file_bad = 'registrations_bad_log.txt'


class Registrations_log:

    def __init__(self, file_inp, file_good, file_bad):
        self.file_inp = file_inp
        self.file_good = file_good
        self.file_bad = file_bad

    def read_file(self):
        self.file_out_good = open(self.file_good, 'w', encoding='utf-8')
        self.file_out_bad = open(self.file_bad, 'w', encoding='utf-8')
        with open(self.file_inp, 'r', encoding='utf-8') as file_inp:
            for line in file_inp:
                try:
                    self._collect_for_line(line=line[:-1])
                except ValueError as exc:
                    if 'unpack' in exc.args[0]:
                        self.file_out_bad.write(f'Не хватает операндов {exc} в строке {line}')
                    else:
                        self.file_out_bad.write(f'Не могу преобразовать к целому {exc} в строке {line}')
                except NotNameError as exc:
                    self.file_out_bad.write(f'{exc} в строке {line}')
                except NotEmailError as exc:
                    self.file_out_bad.write(f'{exc} в строке {line}')
                except ValueageError as exc:
                    self.file_out_bad.write(f'{exc} в строке {line}')
        self.file_out_good.close()
        self.file_out_bad.close()

    def _collect_for_line(self, line):
        name, email, age = line.split(' ')
        age = int(age)
        if not (10 <= age <= 99):
            raise ValueageError('Возраст не входит во временые рамки')
        if not name.isalpha():
            raise NotNameError('Имя имеет небуквенные знаки')
        if not (('@' in email) and ('.' in email)):
            raise NotEmailError('Не стандартный адрес електронной почты')
        self.file_out_good.write(line+'\n')


registrations_log = Registrations_log(file_inp, file_good, file_bad)
registrations_log.read_file()
