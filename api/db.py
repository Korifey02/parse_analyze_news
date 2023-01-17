from motor.motor_asyncio import AsyncIOMotorClient
from beanie import Document, init_beanie
from typing import List


class News(Document):
    title: str
    date: str
    url: str
    body: str

class MarkedNews(Document):
    text: str
    person_non_person: List
    date: str
    url: str

class Tonalty(Document):
    text: str
    ton: str
    person_non_person: List

# class

class DBConnection:
    async def my_init(self):
        client = AsyncIOMotorClient("localhost", 27017, username="root", password="root123")
        await init_beanie(database=client.parser, document_models=[News, MarkedNews, Tonalty])

    async def _if_article_exists(self, url: str):
        return await News.find_one(News.url == url)

    async def insert_article(self, article):
        return await article.insert()

    async def get_n_articles(self, n: int):
        return await News.find().limit(n).to_list()

    async def get_n_articles_marked(self, n: int):
        return await MarkedNews.find().limit(n).to_list()

    async def get_count_news(self):
        return await News.count()

    async def get_ton(self):
        # {"ton": "Negative"}
        return await Tonalty.find().to_list()


connection = DBConnection()