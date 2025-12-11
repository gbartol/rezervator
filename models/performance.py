from sqlalchemy import Integer, String, DateTime, Float
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from models.play import Play
from models.hall import Hall
from models.models import db

class Performance(db.Model):
    # Povezivanje s tablicom 'users' u DB
    __tablename__ = 'performances'

    # Opis svakog stupca
    id_performance: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_play: Mapped[int] = mapped_column(ForeignKey('plays.id_play'))
    id_hall: Mapped[int] = mapped_column(ForeignKey('halls.id_hall'))
    date_performance: Mapped[datetime] = mapped_column(DateTime)
    price_performance: Mapped[float] = mapped_column(Float)

    # Veze između tablica
    play: Mapped[Play] = relationship('Play')
    hall: Mapped[Hall] = relationship('Hall')
