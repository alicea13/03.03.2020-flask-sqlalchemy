import datetime
import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin

from .db_session import SqlAlchemyBase


class Category(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tabletime__ = 'category'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)


class Jobs(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), nullable=True)

    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=0)

    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    start_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

    end_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=False)

    category = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('category.id'), nullable=True)

    categories = orm.relation("Category",
                              secondary='association',
                              backref='jobs')

    def __repr__(self):
        return f'<Job> {self.job}'
