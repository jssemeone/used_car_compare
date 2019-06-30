from flask import current_app
from flask import Flask, render_template
from webapp.news_gibdd import get_gibdd_news


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    @app.route("/")
    def main():
        news_list = get_gibdd_news()
        return render_template('index.html', news_list = news_list)

    return app
