from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from models.user import User
from models.performance import Performance
from models.seat import Seat
from models.models import db

class Reservation(db.Model):
    # Povezivanje s tablicom 'reservations' u DB
    __tablename__ = 'reservations'

    # Opis svakog stupca
    id_reservation: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_user: Mapped[int] = mapped_column(ForeignKey('users.id_user'))
    id_performance: Mapped[int] = mapped_column(ForeignKey('performances.id_performance'))
    id_seat: Mapped[int] = mapped_column(ForeignKey('seats.id_seat'))

    # Veze između tablica
    user: Mapped[User] = relationship('User')
    performance: Mapped[Performance] = relationship('Performance')
    seat: Mapped[Seat] = relationship('Seat')
