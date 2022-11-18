from tech_news.database import db
from search_engine import return_filters
from collections import Counter


# Requisito 10
def top_5_news():
    list_news = list(
        db.news.find(
            {"comments_count":
             {"$gt": 0}}).sort("comments_count", -1))
    return return_filters(list_news[:5])


# Requisito 11
def top_5_categories():
    list_categories = [news["category"]
                       for news
                       in list(db.news.find().sort("category", 1))]
    count = Counter(list_categories).most_common(5)
    list_top_5_categories = [category[0] for category in count]
    return list_top_5_categories
