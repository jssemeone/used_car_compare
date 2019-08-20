from flask import Blueprint, render_template

from webapp.news.models import News

blueprint = Blueprint('news', __name__)


@blueprint.route("/")
def main():
    news_list = News.query.limit(5).all()
    return render_template('news/index.html', news_list = news_list)