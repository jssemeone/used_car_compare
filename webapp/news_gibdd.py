from flask import current_app
import requests
from bs4 import BeautifulSoup
from webapp.model import db, News

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Новости ГИБДД не доступны')
        return False


def get_gibdd_news():
    html = get_html(current_app.config["NEWS_URL"])
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        news_list = soup.find_all(class_="sl-item")
        result_news = []
        for news in news_list:
            title = news.find(class_='sl-item-title').find('a').text
            news_highlight = news.find(class_="sl-item-text").text
            url = "https://xn--90adear.xn--p1ai" + news.find("a")['href']
            published_date = news.find(class_="sl-item-date").text
            published_date = published_date.split()
            published_date = ' '.join(published_date)
            result_news.append({
                'title': title,
                'news_highlight': news_highlight,
                'url': url,
                'published_date': published_date
            })
        return result_news
    return False   

def save_news(title, url, published_date):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        new_news = News(title=title, url=url, published_date=published_date)
        db.session.add(new_news)
        db.session.commit()     