# -*- encoding: utf-8 -*-
import os
import sys
import re
from pymongo import MongoClient
import string
import csv

import findspark
findspark.init()
from pyspark.sql import SparkSession

if not os.path.exists('/word2vec_model'):

    if not os.path.exists('/news/allNews.csv'):

        # start mongodb
        client = MongoClient(host='localhost',
                             port=27017,
                             username='root',
                             password='root123')

        # get news from database
        db = client['parser']
        collection = db.News
        raw_news = collection.find()

        textList = []
        for news in raw_news:
            textList.append(dict({'text': news['title'] + ". " + news['body']}))

        with open("./news/allNews.csv", "w", encoding="utf8") as ds:
            w = csv.DictWriter(ds, delimiter='~', fieldnames=['text'])
            w.writeheader()
            w.writerows(textList)
            i = 0

spark = SparkSession.builder.master("local[*]").getOrCreate()

df = spark.read.csv('./news/allNews.csv',
                    inferSchema=True,
                    header=True,
                    quote="\"",
                    escape="\""
                    )
print(df)
#     # Разбить на токены
#     tokenizer = Tokenizer(inputCol='text', outputCol='words')
#     words = tokenizer.transform(prepared_df)
#
#     # Удалить стоп-слова
#     stop_words = StopWordsRemover.loadDefaultStopWords('russian')
#     remover = StopWordsRemover(inputCol='words', outputCol='filtered', stopWords=stop_words)
#     filtered = remover.transform(words)
#
#     word2Vec = Word2Vec(inputCol='filtered', outputCol='result')
#     model = word2Vec.fit(filtered)
#     w2v_df = model.transform(filtered)
#     w2v_df.show()
#     model.save("/word2vec/word2vec_model")
#
#     #spark.stop()
#
#
# model = Word2VecModel.load('/word2vec/word2vec_model')
#
#
# while True:
#     try:
#         entry_word = input("Введите слово для поиска синонимов:")
#         if entry_word == "-x":
#             break
#         entry_word = entry_word.replace(' ', '')
#         entry_word = entry_word.lower()
#         model.findSynonyms(entry_word, 30).show()
#     except Exception as ex:
#         print("Данного слова нет в словаре!")
#         print(ex)
#
spark.stop()