from tech_news.database import search_news
import datetime


def return_filters(filter):
    return [(news["title"], news["url"]) for news in filter]


def search_by_title(title):
    news_search_title = search_news({"title":
                                    {"$regex": title, "$options": "i"}})
    return return_filters(news_search_title)


# Requisito 7
def search_by_date(date):
    date = datetime.date.fromisoformat(date).strftime("%d/%m/%Y")
    try:
        news_search_date = search_news({"timestamp":
                                       {"$eq": date}})
        return return_filters(news_search_date)
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    news_search_tag = search_news({"tags":
                                  {"$regex": tag, "$options": "i"}})
    return return_filters(news_search_tag)


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
