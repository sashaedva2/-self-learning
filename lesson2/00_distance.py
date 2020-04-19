#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = dict()
moscow=sites['Moscow']
london=sites['London']
paris=sites['Paris']
moscow_london= ((moscow[1] - london[1]) ** 2 + (moscow[2] - london[2]) ** 2) ** 0.5
moscow_paris=((moscow[1] - paris[1]) ** 2 + (moscow[2] - paris[2]) ** 2) ** 0.5
london_paris=((paris[1] - london[1]) ** 2 + (paris[2] - london[2]) ** 2) ** 0.5
# TODO здесь заполнение словаря

print(distances)




