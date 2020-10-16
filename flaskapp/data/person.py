import sqlalchemy as sa
from flaskapp.data.modelbase import SqlAlchemyBase


class Person(SqlAlchemyBase):
    __tablename__ = 'person_tbl'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    first_name = sa.Column(sa.String, nullable=True)
    last_name = sa.Column(sa.String, nullable=True)

    def __repr__(self):
        return f'<Person {self.id}>'
