from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from v1 import schemas, crud

import dependencies

import random

router = APIRouter()


@router.get('/random', response_model=schemas.Joke)
async def get_joke(db: Session = Depends(dependencies.get_db)):
    """
    Get random joke
    :param db:
    :return:
    """
    total = crud.get_number_of_jokes(db)
    if total == 0:
        joke_server = await crud.get_a_new_joke_from_server()
        return crud.create_a_joke(db, joke_server)

    joke_id = random.randint(1, total)
    db_joke = crud.get_a_joke(db, joke_id)

    return db_joke[0]


@router.get('/{joke_id}', response_model=schemas.Joke)
async def get_joke(joke_id: int, db: Session = Depends(dependencies.get_db)):
    """
    Retrieve a joke with a given id. If there is no joke with that id, fetches a new joke from server,
    creates a new joke then returns that joke
    :param joke_id: int
    :return: json
    """
    joke = crud.get_a_joke(db, joke_id)
    if joke is None:
        joke = crud.get_a_new_joke_from_server()
        return crud.create_a_joke(db, joke)
    return joke[0]


