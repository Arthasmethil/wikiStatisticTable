import requests
from bs4 import BeautifulSoup

from config.config import URL


def get_wiki_html(url):
    response = requests.get(url)
    return response


def get_table():
    get_wiki_html(URL)
    get_content = BeautifulSoup(get_wiki_html(URL).content, "html.parser")
    table = get_content.find("table", {"class": "wikitable"})
    return table
