import datetime
import sqlalchemy
from sqlalchemy import orm

from data.db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    passed = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("users.id"))
    task_1 = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    task_2 = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    task_3 = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    task_4 = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    task_5 = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    task_6 = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    task_7 = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    task_8 = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    task_9 = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    task_10 = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    task_11 = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    task_12 = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    task_13 = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    task_14 = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    end = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    user = orm.relationship('User')
