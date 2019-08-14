from datetime import timedelta
import os
basedir = os.path.abspath(os.path.dirname(__file__))

NEWS_URL = "https://xn--90adear.xn--p1ai/news/federal"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
SECRET_KEY = "rfglwerba;ub37AADIhuhhh1122++/=TTj;eevnj"

REMEMBER_COOKIE_DURATION = timedelta(days=5)