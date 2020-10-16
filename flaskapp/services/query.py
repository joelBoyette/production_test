
import pandas as pd
from typing import Optional
from flaskapp.data import db_session
from flaskapp.data.person import Person


def find_person(first: str) -> Optional[Person]:
    session = db_session.create_session()
    return session.query(Person).filter(Person.first_name == first).first()


def create_person(first: str, last: str) -> Optional[Person]:
    if find_person(first):
        return None

    person = Person()
    person.first_name = first
    person.last_name = last

    session = db_session.create_session()
    session.add(person)
    session.commit()

    return person




