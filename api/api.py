from fastapi import APIRouter, Request, Query
from controller import ApiController
from db import connection
import operator
from gensim.models import Word2Vec


router = APIRouter(prefix="/parse")
months = ["Янв", "Фев", "Мар", "Апр", "Май", "Июн", "Июл", "Авг", "Сен", "Окт", "Ноя", "Дек"]


@router.on_event("startup")
async def start_db():
    await connection.my_init()


@router.get("/get_news_of_the_month")
async def get_all_month_news(amount: int = 100, month_you_wanted: str = Query('Дек', enum=months)):
    get_n_articles = await connection.get_n_articles(10000)

    res = []
    for i in range(len(get_n_articles)):
        if len(res) >= amount:
            break
        if month_you_wanted in get_n_articles[i].date:
            res.append(get_n_articles[i])

    return res

@router.get("/get_marked_news")
async def get_marked_news(amount: int = 100):
    get_marked_news = await connection.get_n_articles_marked(amount)
    return get_marked_news

@router.get("/count_news")
async def count_news():
    res = await connection.get_count_news()
    # print(res)
    return {"count": res}

@router.get("/word2vec")
async def get_word_2_vec(word: str):
    # ../ word2vec_model / word2vec.model
    model = Word2Vec.load('../word2vec/word2vec_model/word2vec.model')
    entry_word = word.replace(' ', '')
    entry_word = entry_word.lower()
    try:
        res = model.wv.most_similar(positive=[entry_word], topn=30)
        # print(model.wv.most_similar(positive=[entry_word], topn=30))
    except:
        res = []
    return res


@router.get("/tonalty")
async def get_tonalty():
    res = await connection.get_ton()
    ma_set = set()
    for i in res:
        ma_set.add(i.person_non_person[0])
    print(len(ma_set))
    # print(res)
    return res
