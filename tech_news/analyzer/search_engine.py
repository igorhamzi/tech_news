from tech_news.database import search_news
import datetime


def return_filters(filter):
    return [(news["title"], news["url"]) for news in filter]


def search_by_title(title):
    news_search_title = search_news({"title":
                                    {"$regex": title, "$options": "i"}})
    return return_filters(news_search_title)


def search_by_date(date):
    timestamp = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
    try:
        return [
            (news["title"], news["url"])
            for news in search_news({"timestamp": timestamp})
        ]
    except ValueError:
        raise ValueError("Data inválida")


def search_by_tag(tag):
    news_search_tag = search_news({"tags":
                                  {"$regex": tag, "$options": "i"}})
    return return_filters(news_search_tag)


def search_by_category(category):
    news_search_category = search_news({"category":
                                       {"$regex": category, "$options": "i"}})
    return return_filters(news_search_category)
