from sqlalchemy import select
from sqlalchemy.orm import Session

import requests

from . import models, schemas


def get_a_joke(db: Session, joke_id: int):
    return db.execute(select(models.Joke).where(models.Joke.id == joke_id)).first()



def get_a_new_joke_from_server() -> schemas.JokeCreate:
    """
    gets a random joke from server, checks if it exists. If not, writes it and returns
    :return:
    """
    URL = 'https://api.chucknorris.io/jokes/random'

    joke_from_server = requests.get(URL).json()
    return schemas.JokeCreate(
        id_from_server=str(joke_from_server['id']),
        icon_url=joke_from_server['icon_url'],
        value=joke_from_server['value']
    )


def create_a_joke(db: Session, joke: schemas.JokeCreate):
    joke_to_save = models.Joke(**joke.model_dump())
    db.add(joke_to_save)
    db.commit()
    db.refresh(joke_to_save)
    return joke_to_save


def get_number_of_jokes(db: Session) -> int:
    return db.query(models.Joke).count()
