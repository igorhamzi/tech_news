import requests
import time
from parsel import Selector
from datetime import datetime
from tech_news.database import create_news


def fetch(url):
    for _ in range(15):
        try:
            response = requests.get(url,
                                    headers={"user-agent": "Fake user-agent"},
                                    timeout=3)
            time.sleep(1)
            response.raise_for_status()
        except (requests.Timeout, requests.HTTPError):
            return None
        else:
            return response.text


def scrape_novidades(html_content):
    list_links = []

    list_links.extend(Selector(html_content).css(
                                                "a.cs-overlay-link::attr(href)"
                                                ).getall())

    return list_links


def scrape_next_page_link(html_content):
    next_link = Selector(html_content).css(
                                          "a.next.page-numbers::attr(href)"
                                          ).get()

    return next_link


def scrape_noticia(html_content):
    html = Selector(html_content)
    url = html.css('link[rel=canonical]::attr(href)').get()
    title = html.css('h1.entry-title::text').get().rstrip()
    date = html.css('li.meta-date::text').get()
    date_parsed = datetime.strptime(date, "%d/%m/%Y").strftime("%d/%m/%Y")
    writer = html.css('a.url.fn.n::text').get()
    comments_count = len(html.css('.comment-list li').getall())
    summary = html.css('div.entry-content > p:first-of-type *::text').getall()
    tags = html.css('a[rel=tag]::text').getall()
    category = html.css('span.label::text').get()
    news_report = {
                    'url': url,
                    'title': title,
                    'timestamp': date_parsed,
                    'writer': writer,
                    'comments_count': comments_count,
                    'summary': ''.join(summary).rstrip(),
                    'tags': tags,
                    'category': category
                  }

    return news_report


def get_tech_news(amount):
    url = 'https://blog.betrybe.com/'
    list_news = []

    while len(list_news) < amount:
        html = fetch(url)
        for link in scrape_novidades(html):
            if len(list_news) < amount:
                news_report = scrape_noticia(fetch(link))
                list_news.append(news_report)

        url = scrape_next_page_link(html)

    create_news(list_news)

    return list_news
