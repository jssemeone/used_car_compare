import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Новости ГИБДД не доступны')
        return False


def get_gibdd_news(html):
    html = get_html("https://xn--90adear.xn--p1ai/news/federal")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        news_list = soup.find_all(class_="sl-item")
        result_news = []
        for news in news_list:
            title = news.find(class_='sl-item-title').find('a').text
            news_highlight = news.find(class_="sl-item-text").text
            url = news.find("a")['href']
            published_date = news.find(class_="sl-item-date").text
            result_news.append({
                'title': title,
                'news_highlight': news_highlight,
                'url': url,
                'published_date': published_date
            })
        return result_news
    return False        