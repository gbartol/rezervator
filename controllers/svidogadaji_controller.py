from flask import render_template, request
from models.models import db

from models.performance import Performance
from models.play import Play
from models.hall import Hall
from models.location import Location

class SvidogadajiController:
    def index(self):
        # Dohvatimo sve lokacije i predstave/filmove (trebaju nam za prikaz u formi)
        locations = db.session.execute(db.select(Location.name_location).order_by(Location.name_location)).scalars().all()
        plays = db.session.execute(db.select(Play.title_play).order_by(Play.title_play)).scalars().all()

        # Dohvaćamo podatke iz forme
        location_form = request.form.get('location', default='all_locations')
        play_form = request.form.get('play', default='all_plays')

        # Postavljamo defaultni query na koji kasnije (ovisi o izboru filtera) stavljamo ograničenja
        query = db.select(Performance)

        if( request.method == 'POST' and ( location_form or play_form ) ):

            # Provjerimo je li korisnik odabrao defaultnu 'Sve lokacije' opciju
            if( location_form and ( location_form != 'all_locations' ) ):
                # Ako nije, stavljamo ograničenje za samo lokaciju koju je korisnik odabrao
                # Ispricavam se na ovome, treba spojit 3 tablice pa treba koristit ovo .has()
                query = query.where(
                    Performance.hall.has(
                        Hall.location.has(Location.name_location == location_form)))

            # Provjeravamo je li korisnik odabrao defaultnu 'Svi događaji' opciju
            if( play_form and ( play_form != 'all_plays' ) ):
                # Ako nije, stavljamo ograničenje za samo predstavu/film koju je korisnik odabrao
                query = query.where(
                    Performance.play.has(Play.title_play == play_form))

        # Dohvatimo sve retke iz tablice 'performances' iz baze
        # .scalars() služi da možemo raditi s dohvaćenim podatcima kao s klasama, npr. performance.play.title_play (u svidogadaji.html)
        # https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Result
        # https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.ScalarResult
        performances = db.session.execute(
            query.order_by(Performance.date_performance)).scalars().all()

        # Šaljemo selected_location i selected_play kako bi stvar koju je korisnik odabrao ostala selektirana u formi
        return render_template( 'svidogadaji.html', performances=performances, locations=locations, plays=plays, selected_location=location_form, selected_play=play_form )
