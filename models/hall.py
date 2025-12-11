from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from models.location import Location
from models.models import db

class Hall(db.Model):
    # Povezivanje s tablicom 'users' u DB
    __tablename__ = 'halls'

    # Opis svakog stupca
    id_hall: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_location: Mapped[int] = mapped_column(ForeignKey('locations.id_location'))
    hall_capacity: Mapped[int]

    # Veze između tablica
    location: Mapped[Location] = relationship('Location')
