from webapp import create_app
from webapp.news_gibdd import get_gibdd_news
from webapp.model import db, News

def save_news(title, url, published_date):
    new_news = News(title=title, url=url, published_date=published_date)
    db.session.add(new_news)
    db.session.commit()


if __name__== '__main__':
    app = create_app()
    with app.app_context():
        get_news = get_gibdd_news()
        for news in get_news:
            save_news(news['title'], news['url'], news['published_date'])