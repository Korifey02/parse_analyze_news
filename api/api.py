from fastapi import APIRouter, Request, Query
from controller import ApiController
from db import connection
import operator


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
async def get_marked_news(amount: int = 100, month_you_wanted: str = Query('Дек', enum=months)):
    get_marked_news = await connection.get_n_articles_marked(5000)

    res = []
    for i in range(len(get_marked_news)):
        if len(res) >= amount:
            break
        if month_you_wanted in get_marked_news[i].date:
            res.append(get_marked_news[i])

    return res

@router.get("/count_news")
async def count_news():
    res = await connection.get_count_news()
    # print(res)
    return {"count": res}


