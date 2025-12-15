from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.models import db

class Hall(db.Model):
    # Povezivanje s tablicom 'users' u DB
    __tablename__ = 'halls'

    # Opis svakog stupca
    id_hall: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_location: Mapped[int] = mapped_column(ForeignKey('locations.id_location'))
    capacity_hall: Mapped[int]
    category_hall: Mapped[str] = mapped_column(String(10))

    # Veze između tablica
    location: Mapped['Location'] = relationship('Location')
