import os
import re

os.system("tomitaparser.exe config.proto")
f = open('./output.txt', 'r', encoding='utf-8').readlines()


def getNameFromTags(tags: str) -> str:
    tag = re.findall('<#[A-Z]*\s"*[а-яА-Я0-9]*.*"*\s*-*_*"*"*[а-яА-Я0-9]*.*"*\s*-*_*"*"*[а-яА-Я0-9]*.*"*\s*-*_*"*"*[а-яА-Я0-9]*.*"*\s*-*_*"*"*[а-яА-Я0-9]*.*"*\s*-*_*"*"*[а-яА-Я0-9]*.*"*\s*-*_*"*"*[а-яА-Я0-9]*.*"*\s*-*_*"*#>', tags)[0]
    tag = newTag = re.sub('_', ' ', tag).lower()
    tag = tag.split(' ')
    tag = newTag
    name = re.findall('"*[А-Яа-я0-9]+.*"*\s*-*"*"*[А-Яа-я0-9]*.*"*\s*-*"*"*[А-Яа-я0-9]*.*"*\s*-*"*"*[А-Яа-я0-9]*.*"*\s*-*"*"*[А-Яа-я0-9]*.*"*\s*-*"*"*[А-Яа-я0-9]*.*"*\s*-*"*', tag)
    fullName = ''
    for el in name[0].split(' '):
        el = re.sub("#>", '', el)
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
while line < len(f):
    tagItem = "<#PER "
    if f[line].find('Polit') > -1:
        sentenceTags += str(f[line - 1][:-1])
        while True:
            tagItem += str(f[line + 2][12:-1]) + "#>"
            line += 4
            if line >= len(f) or f[line].find('Polit') == -1:
                break
        tagItem += "\n"
        sentenceTags += tagItem
    if line >= len(f):
        break
    tagItem = "<#PLC "
    if f[line].find('Place') > -1:
        sentenceTags += str(f[line - 1][:-1])
        while True:
            tagItem += str(f[line + 2][9:-1]) + "#>"
            line += 4
            if line >= len(f) or f[line].find('Place') == -1:
                break
        tagItem += "\n"
        sentenceTags += tagItem
    line += 1
# print(sentenceTags)
result = {}
allSentence = re.split('\n', sentenceTags)
result_name = ''
for sentence in allSentence:
    predResultnName = result_name
    result_name = re.split('. <#', sentence)[0]
    if sentence == '': continue
    if re.match('.', sentence).group() == '\t':
        name = getNameFromTags(sentence)
        result[predResultnName].append(name)
        continue
    res = re.split('. <#', sentence)
    result_name = res[0] + '.'
    preTags = '<#' + res[1]
    prePreTags = []
    f = False
    if(preTags.find('#>') != preTags.rfind('#>')):
        nameTag = re.findall('<#[A-Z]*', preTags)[0]
        prePreTags = re.findall('"*[А-Яа-я0-9]+.*"*\s*-*"*"*"*[А-Яа-я0-9]+.*"*\s*-*"*"*"*[А-Яа-я0-9]+.*"*\s*-*"*"*"*[А-Яа-я0-9]+.*"*\s*-*"*#>', preTags)
        for el in prePreTags:
            f = True
            el = nameTag + ' ' + el
            name = getNameFromTags(el)
            if not result_name in result:
                result[result_name] = []
            result[result_name].append(name)
    if f == False:
        name = getNameFromTags(preTags)
        if not result_name in result:
            result[result_name] = []
        result[result_name].append(name)
print(result)
