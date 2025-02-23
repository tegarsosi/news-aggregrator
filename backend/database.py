from tortoise import Tortoise, fields
from tortoise.models import Model


class Category(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, unique=True)

    class Meta:
        table = "categories"


class NewsArticle(Model):
    id = fields.IntField(pk=True)
    title = fields.TextField()
    summary = fields.TextField()
    url = fields.TextField()

    category = fields.ForeignKeyField("models.Category", related_name="articles")

    class Meta:
        table = "news_article"


async def init_db():
    await Tortoise.init(
        db_url="postgres://tegareverest:password@localhost:5432/news_db",
        modules={"models": ["backend.database"]}
    )
    await Tortoise.generate_schemas()
