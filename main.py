from flask import Flask
from data import db_session
from data.users import User
from sqlalchemy import or_
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = "yandex_secret_key"


def main():
    db_session.global_init('db/blogs.sqlite')
    # app.run()

    session = db_session.create_session()

    for user in session.query(User).all():
         print(user)

    # for user in session.query(User).filter((User.id > 1) | (User.email.notilike("%1%"))):
        # print(user)

    for user in session.query(User).filter(or_(User.id > 1) | (User.email.notilike("%1%"))):
        print(user)

    user = session.query(User).filter(User.id == 2).first()
    user.name = "new name"
    user.created_date = datetime.datetime.now()
    session.commit()


if __name__ == '__main__':
    main()
