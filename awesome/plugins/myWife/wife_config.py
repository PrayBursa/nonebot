import random
from .random_config_index import *
import requests
import json
import os


def write(user_list):
    with open('index.json', 'w+', encoding='utf-8') as f:
        src = '['
        for wife in user_list.user_wife_list:
            date = {'name': wife.name,
                    'age': wife.age,
                    'husband': wife.husband,
                    'ouPai': wife.ouPai,
                    'height': wife.height,
                    'widget': wife.widget,
                    'sex': wife.sex,
                    'meng': wife.meng,
                    'isMerry': wife.isMerry,
                    'liking': wife.liking,
                    'work': wife.work,
                    'race': wife.race}
            if len(user_list.user_wife_list) - 1 == user_list.user_wife_list.index(wife):
                src = src + (json.dumps(date, ensure_ascii=False))
            else:
                src = src + (json.dumps(date, ensure_ascii=False) + ',\n')
        src = src + (']')
        f.write(src)
        f.close()


class user:
    def __init__(self, id):
        self.id = id
        self.fuckingBoy = 0


class user_list:
    def __init__(self):
        self.user_wife_list = list()
        self.user = list()
        self.all_user = list()
        self.alredyInit = False

    def add_user(self, wife):
        self.user_wife_list.append(wife)
        self.user.append(wife.husband)


class wife:
    def __init__(self, user):
        f = random.randint(0, len(work) - 1)
        self.work = work[f]

        g = random.randint(0, len(race) - 1)
        self.race = race[g]

        a = random.randint(0, len(surname) - 1)
        b = random.randint(0, len(name) - 1)
        self.name = surname[a] + name[b]

        c = random.randint(0, len(ouPai_size) - 1)
        self.ouPai = ouPai_size[c]

        d = random.randint(16, 24)
        if self.work == '小学生':
            d -= 8
        self.age = d

        e = random.randint(0, len(sex) - 1)
        self.sex = sex[e]

        h = random.randint(145, 170)
        if d >= 16 and h < 150 and not self.race=='矮人' :
            h += 10
        if self.race == '矮人':
            h -= 30
        self.height = str(h)

        i = random.randint(85, 110)
        self.widget = str(i)

        j = random.randint(0, len(mengDian) - 1)
        self.meng = mengDian[j]

        self.husband = user
        self.liking = random.randint(0, 30)
        self.isMerry = False
        self.isTalk = False
        self.scence=get_love_scence()

    def get_merry(self):
        if self.liking >= 50 and self.isMerry == False:
            self.isMerry = True
            a = random.randint(0, len(merry_talk) - 1)
            return merry_talk[a]
        elif self.liking < 50:
            return '我对你的好感度还没那么高，我们进展有点太快了'
        elif self.isMerry:
            return '我们已经结婚了'

    def print_wife_index(self):
        index = '\n' + self.name \
                + ":\n年龄:" \
                + str(self.age) \
                + "\n身高：" + self.height \
                + "\n体重:" + self.widget \
                + "\n欧派:" \
                + self.ouPai \
                + "\n种族:" \
                + self.race \
                + "\n职业:" + self.work + '\n性格：' + self.sex + '\n萌点：' + self.meng \
                + "\n当前好感度:" + str(self.liking)
        return index


def get_love_scence():
    url = 'https://api.uomg.com/api/rand.qinghua'
    date = requests.get(url).json().get('content')
    return date
