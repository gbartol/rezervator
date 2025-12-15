from werkzeug.security import generate_password_hash;
import datetime
from models.models import db

from models.hall import Hall
from models.location import Location
from models.performance import Performance
from models.play import Play
from models.reservation import Reservation
from models.seat import Seat
from models.user import User

class DbController:
    # Kontroler za inicijalizaciju baze podataka.

    '''
    # Zakomentirano, tablice će se kreirati pomoću SQLAlchemy-a

    def create_tables(self):
        # Stvaranje tablica u bazi.
        return db.create_tables();
    '''

    def seed_tables(self):
        # Popunjavanje tablica u bazi testnim podacima.
        try:
            # users:
            ana = User( username='AnaPofuk', password_hash=generate_password_hash('AninaSifra'), email='anapofuk@gmail.com', registration_sequence='abc', has_registered=1  )
            db.session.add( ana )

            franjo = User( username='FranjoSitej', password_hash=generate_password_hash('kucaposo'), email='franjositej@ekrem.hr', registration_sequence='abc', has_registered=1 )
            db.session.add( franjo )

            mance = User( username='MilanManojlovic', password_hash=generate_password_hash('dva'), email='mance@gmail.com', registration_sequence='abc', has_registered=1 )
            db.session.add( mance )

            leon = User( username='LeonLucic', password_hash=generate_password_hash('KrimTim2'), email='lucic@kt2.hr', registration_sequence='abc', has_registered=1  )
            db.session.add( leon )
            # Da iduće tablice mogu iskoristiti id_user
            db.session.flush()


            # plays:
            kosilica = Play( title_play='Kosilica kosi lica', genre_play='horror', duration_play=datetime.time(0, 45), description_play="After Matija inherits his grandfathers vineyard he and his friends soon discover that his grandfather's passing is not so innocent as it seems", category_play='movie' )
            db.session.add( kosilica )

            akordi = Play( title_play='Podzemni Akordi', genre_play='action', duration_play=datetime.time(0, 20), description_play="When three teenage musicians show up to a seemingly empty rehearsal space, they expect nothing more than a jam session. Instead, they uncover a neo-Nazi hideout and a fresh corpse. As they scramble to escape, they're drawn into a violent cat-and-mouse game with a trio of dangerous extremists. What begins as a case of wrong place, wrong time spirals into a nightmarish battle for survival. In the silence between the chords, Podzemni Akordi strikes with tension, dark humor, and a raw portrayal of youth crashing into the brutal realities hidden beneath the surface of everyday life.", category_play='movie' )
            db.session.add( akordi )

            loza = Play( title_play='Đavolja loza', genre_play='slasher', duration_play=datetime.time(0, 40), description_play="Four friends went to the Vineyard to have a good time, but in the air they felt something ominous. Is there something in the air, earth or maybe in the vine?", category_play='movie' )
            db.session.add( loza )
            # Da iduće tablice mogu iskoristiti id_play
            db.session.flush()


            # locations:
            loc1 = Location( name_location='Samobor', address_location='Ulica Mate Lovraka 4' )
            db.session.add( loc1 )

            loc2 = Location( name_location='Kino Tuškanac', address_location='Tuškanac 1' )
            db.session.add( loc2 )
            # Da iduće tablice mogu iskoristiti id_location
            db.session.flush()


            # halls:
            hall1 = Hall( location=loc1, capacity_hall=100, category_hall='movie' )
            db.session.add( hall1 )

            hall2 = Hall( location=loc2, capacity_hall=80, category_hall='movie' )
            db.session.add( hall2 )
            # Da iduće tablice mogu iskoristiti id_hall
            db.session.flush()


            # performances:
            per1 = Performance( play=kosilica, hall=hall1, date_performance=datetime.datetime(2026, 2, 7, 17, 50), price_performance=10.00 )
            db.session.add( per1 )

            per2 = Performance( play=kosilica, hall=hall2, date_performance=datetime.datetime(2026, 2, 7, 19), price_performance=10 )
            db.session.add( per2 )

            per3 = Performance( play=akordi, hall=hall1, date_performance=datetime.datetime(2026, 1, 24, 17), price_performance=7 )
            db.session.add( per3 )

            per4 = Performance( play=akordi, hall=hall2, date_performance=datetime.datetime(2026, 1, 24, 17, 45), price_performance=7 )
            db.session.add( per4 )

            per5 = Performance( play=loza, hall=hall1, date_performance=datetime.datetime(2026, 2, 6, 17), price_performance=8 )
            db.session.add( per5 )

            per6 = Performance( play=loza, hall=hall1, date_performance=datetime.datetime(2026, 2, 6, 17, 45), price_performance=8 )
            db.session.add( per6 )
            # Da iduće tablice mogu iskoristiti id_performance
            db.session.flush()


            # seats:
            hall1_seats = []
            for i in range(1,11):
                for j in range(1,11):
                    seat = Seat( hall=hall1, row_seat=i, column_seat=j )
                    db.session.add( seat )
                    hall1_seats.append(seat)

            hall2_seats = []
            for i in range(1,11):
                for j in range(1,9):
                    seat = Seat( hall=hall2, row_seat=i, column_seat=j )
                    db.session.add( seat )
                    hall2_seats.append(seat)
            # Da iduće tablice mogu iskoristiti id_seat
            db.session.flush()


            # reservations:
            res1 = Reservation( user=ana, performance=per1, seat=hall1_seats[0], date_reservation=datetime.datetime(2025, 12, 10, 23, 46) )
            db.session.add( res1 )

            res2 = Reservation( user=ana, performance=per1, seat=hall1_seats[1], date_reservation=datetime.datetime(2025, 11, 1, 21, 10) )
            db.session.add( res2 )

            res3 = Reservation( user=franjo, performance=per1, seat=hall1_seats[5], date_reservation=datetime.datetime(2025, 12, 26, 19, 31) )
            db.session.add( res3  )

            res4 = Reservation( user=mance, performance=per1, seat=hall1_seats[8], date_reservation=datetime.datetime(2025, 11, 17, 8, 8) )
            db.session.add( res4 )

            res5 = Reservation( user=leon, performance=per2, seat=hall1_seats[0], date_reservation=datetime.datetime(2025, 12, 25, 3, 15) )
            db.session.add( res5 )

            res6 = Reservation( user=franjo, performance=per2, seat=hall1_seats[6], date_reservation=datetime.datetime(2025, 11, 23, 15, 28) )
            db.session.add( res6 )

            # Commitamo sve promjene:
            db.session.commit()
            return 'Database seeded successfully!'

        except Exception as e:
            db.session.rollback()
            return f'Error seeding database: {str(e)}'
