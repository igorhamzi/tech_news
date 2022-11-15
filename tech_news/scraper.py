import requests
import time


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


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
