from flask import Flask
from data import db_session
from data.user import User
from data.news import News
from sqlalchemy import or_
import datetime

from data.users import Users

app = Flask(__name__)
app.config['SECRET_KEY'] = "yandex_secret_key"


def main():
    db_session.global_init('db/blogs.sqlite')

    user = Users()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief2@mars.org"
    session = db_session.create_session()
    session.add(user)
    session.commit()

    user = Users()
    user.surname = "Kaupers"
    user.name = "Andre"
    user.age = 27
    user.position = "flight engineer"
    user.speciality = "equilibrium research"
    user.address = "Amsterdam, Holland"
    user.email = "andre_kaupers@mars.org"
    session = db_session.create_session()
    session.add(user)
    session.commit()

    user = Users()
    user.surname = "Donald"
    user.name = "Pettit"
    user.age = 46
    user.position = "flight engineer-2"
    user.speciality = "chemical engineering"
    user.address = "Oregon, USA"
    user.email = "pettit_d@mars.org"
    session = db_session.create_session()
    session.add(user)
    session.commit()

    user = Users()
    user.surname = "Kononenko"
    user.name = "Oleg"
    user.age = 44
    user.position = "commander"
    user.speciality = "mechanical engineer"
    user.address = "Chardzhou city, Turkmenistan"
    user.email = "konon_oleg.org"
    session = db_session.create_session()
    session.add(user)
    session.commit()


if __name__ == '__main__':
    main()
