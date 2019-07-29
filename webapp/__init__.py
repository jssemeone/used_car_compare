from webapp.model import db, News
from flask import Flask, render_template
from webapp.forms import LoginForm


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)

    @app.route("/")
    def main():
        news_list = News.query.limit(5).all()
        return render_template('index.html', news_list = news_list)

    @app.route('/login')
    def login():
        title = "Авторизация"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    return app
