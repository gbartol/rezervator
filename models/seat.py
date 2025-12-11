from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from models.hall import Hall
from models.models import db

class Seat(db.Model):
    # Povezivanje s tablicom 'users' u DB
    __tablename__ = 'seats'

    # Opis svakog stupca
    id_seat: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_hall: Mapped[int] = mapped_column(ForeignKey('halls.id_hall'))
    row_seat: Mapped[int]
    column_seat: Mapped[int]

    # Veze između tablica
    hall: Mapped[Hall] = relationship('Hall')
