# -*- coding: utf-8 -*-
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor
import argparse


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru
# def make_ticket(fio='Слободянюк А.О.', from_='Москва', to='Море', date='21.07', save=None):

def make_ticket(fio, from_, to, date, save=None):
    font_path = os.path.join("C:\\Users\\sasha\\PycharmProjects\\-self-learning\\lesson13\\fonts", "timesbd.ttf")
    template = "ticket_template.jpg"
    im = Image.open(template)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(font_path, size=15)
    y = im.size[1] - 140  # - (10 + font.size) * 2
    draw.text((47, y - 135), fio, font=font, fill=ImageColor.colormap['black'])
    draw.text((47, y - 65), from_, font=font, fill=ImageColor.colormap['black'])
    draw.text((47, y), to, font=font, fill=ImageColor.colormap['black'])
    draw.text((287, y), date, font=font, fill=ImageColor.colormap['black'])
    out_path = save if save else 'probe.jpg'
    im.save(out_path)
    print(f'Post card saved as {out_path}')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-F", "--fio", required=True,
                    help="name, last name et al")
    ap.add_argument("-f", "--from", required=True,
                    help="place of departure")
    ap.add_argument("-t", "--to", required=True,
                    help="place of arrival")
    ap.add_argument("-d", "--date", required=True,
                    help="date of travel")
    ap.add_argument("-s", "--save_to", required=False,
                    help="save file")
    args = vars(ap.parse_args())
    make_ticket(fio=args['fio'], from_=args['from'], to=args['to'], date=args['date'], save=args['save_to'])

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
