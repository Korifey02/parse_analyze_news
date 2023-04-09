from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag
import pickle
from pathlib import Path
from pymongo import MongoClient
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_ru')
nltk.download('stopwords')

import re, string, random


def remove_noise(tweet_tokens, stop_words=()):
    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|' \
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', token)
        token = re.sub("(@[A-Za-z0-9_]+)", "", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens


def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token


def get_tweets_for_model(cleaned_tokens_list):
    for tweet_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tweet_tokens)


def __main__():
    import nltk
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger_ru')
    nltk.download('stopwords')
    model_file = Path('classifier.pickle')

    # Подключаемся к базе данных
    client = MongoClient("localhost", 27017, username="root", password="root123")
    db = client.parser
    collection = db['MarkedNews']
    cursor = collection.find({})

    # Подключае модель и необходимые элементы анализа
    f = open('classifier.pickle', 'rb')
    classifier = pickle.load(f)
    f.close()

    for document in cursor:
        _id = document["_id"]
        tweet = document["text"]
        person = document["person_non_person"]
        string = ""

        custom_tokens = remove_noise(word_tokenize(tweet))
        string = classifier.classify(dict([token, True] for token in custom_tokens))

        new_collection = db.Tonalty

        if new_collection.find_one({"_id": _id}):
            continue

        new_collection.insert_one(
            {
                '_id': _id,
                'text': tweet,
                'ton': string,
                'person_non_person': person
            }
        )


if __name__ == "__main__":
    __main__()