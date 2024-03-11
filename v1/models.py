from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Joke(Base):
    __tablename__ = 'joke'

    id: Mapped[int] = mapped_column(primary_key=True)
    id_from_server: Mapped[str]
    icon_url: Mapped[str]
    value: Mapped[str]
