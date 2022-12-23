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
async def get_all_month_news(amount: int = 100, month_you_wanted: str = Query('Янв', enum=months)):
    # res = await connection._if_article_exists("https://gorvesti.ru/society/v-volgograde-nagradili-medalyami-sotrudnikov-rosgvardii-za-otvagu-v-svo-126085.html")
    get_n_articles = await connection.get_n_articles(5000)

    res = []
    for i in range(len(get_n_articles)):
        if len(res) >= amount:
            break
        if month_you_wanted in get_n_articles[i].date:
            res.append(get_n_articles[i])

    return res




    # return {"message": f"{month_you_wanted}"}
