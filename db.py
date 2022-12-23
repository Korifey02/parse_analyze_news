from motor.motor_asyncio import AsyncIOMotorClient
from beanie import Document, init_beanie


class News(Document):
    title: str
    date: str
    url: str
    body: str


class DBConnection:
    async def my_init(self):
        client = AsyncIOMotorClient("localhost", 27017, username="root", password="root123")
        await init_beanie(database=client.parser, document_models=[News])

    async def _if_article_exists(self, url: str):
        return await News.find_one(News.url == url)

    async def insert_article(self, article):
        return await article.insert()

    async def get_n_articles(self, n: int):
        return await News.find().limit(n).to_list()

    async def get_count_news(self):
        return await News.count()


connection = DBConnection()