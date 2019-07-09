from flask import current_app
from webapp.model import db, News
from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    @app.route("/")
    def main():
        news_list = News.query.all()
        return render_template('index.html', news_list = news_list)

    return app
