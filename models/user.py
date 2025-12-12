from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from models.models import db

class User(db.Model):
    # Povezivanje s tablicom 'users' u DB
    __tablename__ = 'users'

    # Opis svakog stupca
    id_user: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50))
    password_hash: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(50))
    registration_sequence: Mapped[str] = mapped_column(String(20))
    has_registered: Mapped[int]

    # Veze između tablica
    reservations: Mapped[list['Reservation']] = relationship('Reservation', back_populates='user')
