import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Jobs():
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    position = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True)

    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    collaborators = sqlalchemy.Column(sqlalchemy.L)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                      default=datetime.datetime.now)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                      default=datetime.datetime)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean)

    news = orm.relation("News", back_populates='user')

    def __repr__(self):
        return f'<{self.__class__.__name__}> {self.name} {self.email}'


# как задать тип список в столбце
# установить связь с помощбю relationship?