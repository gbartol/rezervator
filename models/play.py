from sqlalchemy import Integer, String, Time
from datetime import time
from sqlalchemy.orm import Mapped, mapped_column
from models.models import db
 class Play(db.Model):
    # Povezivanje s tablicom 'plays' u DB
    __tablename__ = 'plays'

    # Opis svakog stupca
    id_play: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title_play: Mapped[str] = mapped_column(String(140))
    genre_play: Mapped[str] = mapped_column(String(140))
    duration_play: Mapped[time] = mapped_column(Time)
    description_play: Mapped[str] = mapped_column(String(1000))
