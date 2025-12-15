from flask import render_template
from pymysql.err import MySQLError
from models.models import db

from models.performance import Performance
from models.play import Play

class SvidogadajiController:
    def index(self):
        # Inicijaliziramo listu 'performances' na praznu listu
        performances = []

        performances = db.session.execute(db.select(Performance)).scalars().all()

        return render_template( 'svidogadaji.html', performances=performances )
