# -*- encoding: utf-8 -*-
import os
import sys
import re

import nltk as nltk
from nltk.corpus import stopwords

from pymongo import MongoClient

from gensim.models import Word2Vec

import pymorphy2

import string
import csv


if not os.path.exists('./word2vec_model/word2vec.model'):
    # start mongodb
    client = MongoClient(host='localhost',
                         port=27017,
                         username='root',
                         password='root123')
    # get news from database
    db = client['parser']
    collection = db.News
    raw_news = collection.find()
    articleList = []
    textList = []
    for news in raw_news:
        text = news['title'] + '. ' + news['body']
        text = re.sub('[^а-яА-Яa-zA-Z]', ' ', text)
        articleList.append(text.lower())
    j  = 1
    for text in articleList:
        allSent = nltk.sent_tokenize(text)
        for el in allSent:
            print(j)
            el = re.sub('[^а-яА-Яa-zA-Z]', ' ', el)
            textList.append(el)
            j += 1
    all_words = [nltk.word_tokenize(text) for text in textList]
    stop_words = stopwords.words('russian')
    morph = pymorphy2.MorphAnalyzer()
    for i in range(len(all_words)):
        print(i)
        all_words[i] = [morph.parse(word)[0].normal_form for word in all_words[i] if word not in stop_words]
    print('start')
    model = Word2Vec(all_words, vector_size=500, window=10, min_count=2, sg=1)
    model.train(all_words, total_examples=model.corpus_count, epochs=30, report_delay=1)
    print('end')
    model.save("./word2vec_model/word2vec.model")

print('''MODEL IS SUCCESS INSTALLED''')

model = Word2Vec.load("./word2vec_model/word2vec.model")
print(model.wv.most_similar(positive=['украина'], topn=10))