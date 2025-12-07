from flask import render_template
from pymysql.err import MySQLError
from db import get_db_connection

class SvidogadajiController:
    def index(self):
        # Inicijaliziramo listu 'dogadaji' na praznu listu
        dogadaji = []

        try:
            # Spajamo se na bazu
            db = get_db_connection()
            cursor = db.cursor()

            # TODO: Osmisliti bazu podataka, napisati SQL naredbe...

            return render_template( 'kazaliste.html', dogadaji=dogadaji, msg='' )

        except MySQLError as err:
            return render_template( 'svidogadaji.html', dogadaji=dogadaji, msg=err )
