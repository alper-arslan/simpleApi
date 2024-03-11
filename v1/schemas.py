from typing import Optional

from pydantic import BaseModel


class JokeBase(BaseModel):
    pass

    class Config:
        from_attributes = True


class Joke(JokeBase):
    id: int
    id_from_server: str
    icon_url: Optional[str] = None
    value: str


class JokeCreate(JokeBase):
    id_from_server: str
    icon_url: Optional[str] = None
    value: str
