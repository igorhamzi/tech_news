import requests
import time
from parsel import Selector


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


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
