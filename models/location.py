from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from models.models import db

class Location(db.Model):
    # Povezivanje s tablicom 'users' u DB
    __tablename__ = 'locations'

    # Opis svakog stupca
    id_location: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name_location: Mapped[str] = mapped_column(String(140))
    address_location: Mapped[str] = mapped_column(String(500))
