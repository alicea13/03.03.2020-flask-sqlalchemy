from flask import Flask
from data import db_session
from  data.users import User
from sqlalchemy import or_


app = Flask(__name__)
app.config['SECRET_KEY'] = "yandex_secret_key"


def main():
    db_session.global_init('db/mars_explorer.db')

if __name__ == '__main__':
    main()
