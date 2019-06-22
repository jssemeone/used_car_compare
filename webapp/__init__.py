from flask import Flask, render_template


app = Flask(__name__)
from webapp.news_gibdd import get_gibdd_news

@app.route("/")
def main():
    news_list = get_gibdd_news
    return render_template('index.html', news_list = news_list)

if __name__ == "__main__":
    app.run()