from tech_news.database import db
from search_engine import return_filters


# Requisito 10
def top_5_news():
    list_news = list(
        db.news.find(
            {"comments_count":
             {"$gt": 0}}).sort("comments_count", -1))
    return return_filters(list_news[:5])


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
