import asyncio
from backend.database import init_db, Category, NewsArticle


async def populate_data():
    await init_db()

    # Fetch existing categories
    tech = await Category.get(name="Technology")
    politics = await Category.get(name="Politics")

    # Insert new sample articles
    await NewsArticle.create(
        title="New Quantum Computing Breakthrough",
        summary="Scientists achieve major milestone in quantum computing research.",
        url="https://technews.com/quantum",
        category=tech
    )

    await NewsArticle.create(
        title="Global Climate Summit Results",
        summary="World leaders agree on new environmental protection measures.",
        url="https://news.com/climate-summit",
        category=politics
    )

    await NewsArticle.create(
        title="Latest Developments in Machine Learning",
        summary="New algorithms show promising results in natural language processing.",
        url="https://technews.com/ml-update",
        category=tech
    )

asyncio.run(populate_data())
