import os
import re

from pymongo import MongoClient


def getNameFromTags(tags: str) -> str:
    tag = newTag = re.sub('_', ' ', tags).lower()
    tag = newTag
    name = re.findall('"*[А-Яа-я0-9]+.*"*\s*-*"*"*[А-Яа-я0-9]*.*"*\s*-*"*"*[А-Яа-я0-9]*.*"*\s*-*"*"*[А-Яа-я0-9]*.*"*\s*-*"*"*[А-Яа-я0-9]*.*"*\s*-*"*"*[А-Яа-я0-9]*.*"*\s*-*"*', tag)
    fullName = ''
    for el in name[0].split(' '):
        if el[0] == '"':
            fullName += '"' + el[1].upper() + el[2::] + ' '
            continue
        if el[1] == '.':
            fullName += el[0].upper() + el[1] + el[2].upper() + el[3] + el[4].upper() + el[5::] + ' '
            continue
        fullName += el[0].upper() + el[1::] + ' '
    fullName = re.sub('Он.', 'им.', fullName)
    name = fullName[:len(fullName) - 1:]
    return name


client = MongoClient(host='localhost',
                     port=27017,
                     username='root',
                     password='root123')

db = client['parser']
collection = db.News
raw_news = collection.find(no_cursor_timeout=True).skip(6500)
cnt_news = 10006

for news in raw_news:
    try:
        print(cnt_news)
        f = open('./input.txt', 'w', encoding='utf-8')
        f.write(news['title'] + ' ' + news['body'])
        f.close()

        os.system("tomitaparser.exe config.proto")

        f = open('./output.txt', 'r', encoding='utf-8').readlines()

        line = 0
        sentenceTags = ""
        sentence = ""
        result = {}
        while line < len(f):
            if f[line].find('Polit') > -1:
                sentence += str(f[line - 1][:-1])
                while True:
                    name = ""
                    name += str(f[line + 2][12:-1])
                    line += 4
                    name = getNameFromTags(name)
                    if not sentence in result:
                        result[sentence] = []
                    result[sentence].append(name)
                    if line >= len(f) or f[line].find('Polit') == -1:
                        break
                if not sentence in result:
                    result[sentence] = []
                result[sentence].append(name)
            if line >= len(f):
                break
            if f[line].find('Place') > -1:
                sentence += str(f[line - 1][:-1])
                while True:
                    name = ""
                    name += str(f[line + 2][9:-1])
                    line += 4
                    name = getNameFromTags(name)
                    if not sentence in result:
                        result[sentence] = []
                    result[sentence].append(name)
                    if line >= len(f) or f[line].find('Place') == -1:
                        break
            line += 1

        ### Added data to db
        if len(result) > 0:
            MarkedNews = db.MarkedNews
            for el in result:
                if MarkedNews.find_one({'url': news['url']}): continue
                else:
                    MarkedNews.insert_one(
                        {
                            'text': el,
                            'person_non_person': result[el],
                            'date': news['date'],
                            'url': news['url'],

                        }
                        )
                    print('IS ADDED. OK.')

        cnt_news += 1
    except Exception as e:
        f = open('./errors', 'w', encoding='utf-8')
        f.write(f'1.{news}\nОшибка:{e}\n')
        f.close()
        continue

raw_news.close()
