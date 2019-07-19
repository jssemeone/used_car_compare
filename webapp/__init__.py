from webapp.model import db, News
from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)

    @app.route("/")
    def main():
        news_list = News.query.limit(7).all()
        return render_template('index.html', news_list = news_list)

    return app
