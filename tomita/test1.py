import os
import re

os.system("tomitaparser.exe config.proto")
f = open('./output.txt', 'r', encoding='utf-8').readlines()


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
print(result)
