import db;

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
        return db.seed_tables();

