from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
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
    user: Mapped['User'] = relationship('User', back_populates='reservations')
    performance: Mapped['Performance'] = relationship('Performance', back_populates='performances')
    seat: Mapped['Seat'] = relationship('Seat')
