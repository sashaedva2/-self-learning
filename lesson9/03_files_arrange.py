# -*- coding: utf-8 -*-

import os, time, shutil


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2



class Files_arrange:

    def __init__(self, dirname, newdir):
        self.dirname = dirname
        self.newdir = newdir
        if os.path.isdir(newdir):
            shutil.rmtree(newdir)

    def arrange(self):
        for d, dirs, files in os.walk(self.dirname):
            for f in files:
                self.distribution(os.path.join(d, f))  # формирование адреса, добавление адреса в список

    def distribution(self, path):
        self.link = os.path.basename(os.path.dirname(path))
        self.date = time.gmtime(os.path.getmtime(path))
        self.directory = self.newdir + '\{0}\{1}\{2}'.format(self.link, self.date.tm_year, self.date.tm_mon)
        if not os.path.isdir(self.directory):
            os.makedirs(self.directory)
        shutil.copy2(path, self.directory)

files_arrange = Files_arrange('G:\icons', 'G:\icons_by_year')
files_arrange.arrange()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
