# -*- coding: utf-8 -*-
import pandas as pd
import os
from collections import defaultdict
from utils import time_track
import multiprocessing


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
class Volatility(multiprocessing.Process):

    def __init__(self, dirname, collector, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dirname = dirname
        self.collector = collector

    def run(self):
        self.data = pd.read_csv(self.dirname, sep=',', encoding='cp1251')
        price = self.data['PRICE']
        average_price = (price.max() + price.min()) / 2
        self.volatility = ((price.max() - price.min()) / average_price) * 100
        self.flag = self.data['SECID'][0]
        self.collector.put(dict(flag=self.flag, volatility=self.volatility))


def vivod_max_min(func, dictionary):
    mode = func(dictionary, key=dictionary.get)
    print(f'    {mode} - {dictionary.pop(mode)} %')
    mode = func(dictionary, key=dictionary.get)
    print(f'    {mode} - {dictionary.pop(mode)} %')
    mode = func(dictionary, key=dictionary.get)
    print(f'    {mode} - {dictionary.pop(mode)} %')


@time_track
def main():
    files_all = list()
    dict_volatil = defaultdict(int)
    collector = multiprocessing.Queue()
    for d, dirs, files in os.walk('trades'):
        for f in files:
            files_all.append(os.path.join(d, f))

    volats = [Volatility(dirname=dirname, collector=collector) for dirname in files_all]

    for volat in volats:
        volat.start()
    try:
        for volat in volats:
            volat.join()
    except Exception as exc:
        print(exc)
    while not collector.empty():
        database = collector.get()
        dict_volatil[database['flag']] = round(database['volatility'], 2)
        print(f"{database['flag']}: Тикет обработан", flush=True)

    print('Максимальная волатильность:')
    vivod_max_min(max, dict_volatil)

    keys = [k for k, v in dict_volatil.items() if v == 0]
    for key in keys:
        dict_volatil.pop(key)

    print('Минимальная волатильность:')
    vivod_max_min(min, dict_volatil)

    print('Нулевая волатильность:')
    str = ''
    for key in keys:
        str += key + ', '
    print(f'    {str}')


if __name__ == '__main__':
    main()
