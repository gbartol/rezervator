from flask import g, current_app;
import pymysql;
from pymysql.err import MySQLError;
from werkzeug.security import generate_password_hash, check_password_hash;

def get_db_connection():
    if( 'db_connection' not in g ):
        g.db_connection = pymysql.connect(
            host=current_app.config['DATABASE_HOST'],
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASS'],
            database=current_app.config['DATABASE_DB'],
            cursorclass=pymysql.cursors.DictCursor
        );

    return g.db_connection;


def close_db( error ):
    db = g.pop( 'db_connection', None );
    if( db is not None ):
        db.close();


def prepare_db():
    msg = '';

    try:
        if( has_tables() ):
            return 'Tablice dz2_users/dz2_follows/dz2_quacks već postoje u bazi. Obrišite ih i probajte ponovno.'

# -------------------- TODO: Zamijeniti ovo sa stvarnim tablicama koje ćemo koristiti

        # Kreiraj tablice u bazi podataka.
        msg += create_table_users() + '<br>';
        msg += create_table_follows() + '<br>';
        msg += create_table_quacks() + '<br>';

        # Popuni tablice u bazi podataka.
        msg += seed_table_users() + '<br>';
        msg += seed_table_follows() + '<br>';
        msg += seed_table_quacks() + '<br>';

    except MySQLError as err:
        return f'{msg}\nerror: {err}';

    return msg;


def has_tables():
    db = get_db_connection();
    cursor = db.cursor();

    ret = False;
    sql = 'SHOW TABLES LIKE %(tblname)s';

    cursor.execute( sql, {'tblname': 'dz2_users'} );
    if( cursor.rowcount > 0 ):
        ret = True;

    cursor.execute( sql, {'tblname': 'dz2_follows'} );
    if( cursor.rowcount > 0 ):
        ret = True;

    cursor.execute( sql, {'tblname': 'dz2_quacks'} );
    if( cursor.rowcount > 0 ):
        ret = True;

    cursor.close();
    return ret;



def create_table_users():
    # Stvori tablicu users.
    # Svaki user ima svoj id (automatski će se povećati za svakog novoubačenog korisnika), korisničko ime, password hash, email,
    # slučajan niz znakova potreban za registraciju, te oznaku je li registracija uspješno dovršena.
    db = get_db_connection();
    cursor = db.cursor();

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS users (' +
        'id_user int NOT NULL PRIMARY KEY AUTO_INCREMENT,' +
        'username varchar(50) NOT NULL,' +
        'password_hash varchar(255) NOT NULL,' +
        'email varchar(50) NOT NULL,' +
        'registration_sequence varchar(20) NOT NULL,' +
        'has_registered int)' );

    db.commit();
    cursor.close();

    return f'create_table_users: OK';


def create_table_reservations():
    # Stvori tablicu follows.
    # Za svako "praćenje" pamtimo id korisnika, te id korisnika koji ga prati.
    db = get_db_connection();
    cursor = db.cursor();

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS reservations(' +
        'id_reservation int NOT NULL PRIMARY KEY AUTO_INCREMENT,' +
        'id_user int NOT NULL FOREIGN KEY,' +
        'id_performance int NOT NULL FOREIGN KEY,' +
        'id_seat int NOT NULL FOREIGN KEY');

    db.commit();
    cursor.close();

    return f'create_table_reservations: OK';


def create_table_plays():
    db = get_db_connection();
    cursor = db.cursor();

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS plays(' +
        'id_play int NOT NULL PRIMARY KEY AUTO_INCREMENT,' +
        'title_play varchar(140) NOT NULL,' +
        'genre_play varchar(140) NOT NULL,' +
        'duration_play TIME NOT NULL,' +
        'description_play varchar(1000))' );

    db.commit();
    cursor.close();

    return f'create_table_plays: OK';


def create_table_performances():
    db = get_db_connection();
    cursor = db.cursor();

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS performances(' +
        'id_performance int NOT NULL PRIMARY KEY AUTO_INCREMENT,' +
        'id_play int NOT NULL FOREIGN KEY,' +
        'id_hall int NOT NULL FOREIGN KEY,' +
        'date_performance DATETIME NOT NULL,' +
        'price_performance float(10))' )# TODO: vidjeti je li radi, ako ne probati s decimal

    db.commit();
    cursor.close();

    return f'create_table_performances: OK';


def create_table_halls():
    db = get_db_connection();
    cursor = db.cursor();

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS halls(' +
        'id_hall int NOT NULL PRIMARY KEY AUTO_INCREMENT,' +
        'id_location int NOT NULL FOREIGN KEY,' +
        'hall_capacity int)' );

    db.commit();
    cursor.close();

    return f'create_table_halls: OK';


def create_table_locations():
    db = get_db_connection();
    cursor = db.cursor();

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS locations(' +
        'id_location int NOT NULL PRIMARY KEY AUTO_INCREMENT,' +
        'name_location varchar(140) NOT NULL,' +
        'address_location varchar(500) NOT NULL)' );

    db.commit();
    cursor.close();

    return f'create_table_halls: OK';


def create_table_seats():
    db = get_db_connection();
    cursor = db.cursor();

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS seats(' +
        'id_seat int NOT NULL PRIMARY KEY AUTO_INCREMENT,' +
        'id_hall int NOT NULL FOREIGN KEY,' +
        'row_seat int NOT NULL,' +
        'column_seat int NOT NULL' );

    db.commit();
    cursor.close();

    return f'create_table_seats: OK';


def seed_table_users():
    # Uočimo da ne treba specificirati id koji se automatski poveća kod svakog ubacivanja.
    db = get_db_connection();
    cursor = db.cursor();

    sql = 'INSERT INTO rezervator_users(username, password_hash, email, registration_sequence, has_registered) VALUES (%(username)s, %(password)s, \'a@b.com\', \'abc\', \'1\')';

    cursor.execute( sql,
        {'username': 'AnaPofuk', 'password': generate_password_hash( 'AninaSifra' ) } );

    cursor.execute( sql,
        {'username': 'FranjoSitej', 'password': generate_password_hash( 'kucaposo' ) } );

    cursor.execute( sql,
        {'username': 'MilanManojlovic', 'password': generate_password_hash( 'dva' ) } );

    cursor.execute( sql,
        {'username': 'LeonLucic', 'password': generate_password_hash( 'KrimTim2' ) } );

    db.commit();
    cursor.close();

    return f'seed_table_users: OK';


def seed_table_reservations():
    db = get_db_connection();
    cursor = db.cursor();
    
    sql = 'INSERT INTO rezervator_reservations(id_user, id_performance, id_seat) VALUES (%(id_user)s, %(id_performance)s, %(id_seat)s)'

    cursor execute (sql , 
        {'id_user': '1', 'id_performance': '1', 'id_seat' : '1'})
    cursor execute (sql , 
        {'id_user': '1', 'id_performance': '1', 'id_seat' : '2'})
    cursor execute (sql , 
        {'id_user': '2', 'id_performance': '1', 'id_seat' : '4'})
    cursor execute (sql , 
        {'id_user': '3', 'id_performance': '1', 'id_seat' : '7'})
    cursor execute (sql , 
        {'id_user': '4', 'id_performance': '2', 'id_seat' : '1'})
    cursor execute (sql , 
        {'id_user': '5', 'id_performance': '2', 'id_seat' : '5'})

    db.commit();
    cursor.close();

    return f'seed_table_reservations: OK';



def seed_table_plays():
    db = get_db_connection();
    cursor = db.cursor();

    
    sql = 'INSERT INTO rezervator_plays(title_play, genre_play, duration_play, description_play) VALUES (%(title)s, %(genre)s, %(duration)s, %(description)s)'

    cursor execute (sql, 
        {'title' : 'Kosilica kosi lica', 'genre' : 'horror', 'duration' : '45',
        'description' : "After Matija inherits his grandfathers vineyard he and his friends soon discover that his grandfather's passing is not so innocent as it seems"}
        )

    cursor execute (sql, 
        {'title' : 'Podzemni Akordi', 'genre' : 'action', 'duration' : '20',
        'description' : "When three teenage musicians show up to a seemingly empty rehearsal space, they expect nothing more than a jam session. Instead, they uncover a neo-Nazi hideout and a fresh corpse. As they scramble to escape, they're drawn into a violent cat-and-mouse game with a trio of dangerous extremists. What begins as a case of wrong place, wrong time spirals into a nightmarish battle for survival. In the silence between the chords, Podzemni Akordi strikes with tension, dark humor, and a raw portrayal of youth crashing into the brutal realities hidden beneath the surface of everyday life."})

    cursor execute (sql, 
        {'title' : 'Đavolja loza', 'genre' : 'slasher', 'duration' : '40',
        'description' : "Four friends went to the Vineyard to have a good time, but in the air they felt something ominous. Is there something in the air, earth or maybe in the vine?"   
        })
    db.commit();
    cursor.close();

    return f'seed_table_plays: OK';


def seed_table_performances():
    db = get_db_connection();
    cursor = db.cursor();
    
    sql = 'INSERT INTO rezervator_performances(id_play, id_hall, date_performance, price_performance) VALUES (%(id_play)s, %(id_hall)s, %(date)s, %(price)s)'

    cursor execute (sql ,
        {'id_play' : '1', 'id_hall' : '1' , 'date' : '2026-02-07 17:50:00', 'price' : '10' }) 

    cursor execute (sql ,
        {'id_play' : '1', 'id_hall' : '2',  'date' : '2026-02-07 19:00:00', 'price' : '10' }) 

    cursor execute (sql ,
        {'id_play' : '2', 'id_hall' : '1',  'date' : '2026-01-24 17:00:00', 'price' : '7' }) 

    cursor execute (sql ,
        {'id_play' : '2', 'id_hall' : '2',  'date' : '2026-01-24 17:45:00', 'price' : '7' })

    cursor execute (sql ,
        {'id_play' : '3', 'id_hall' : '1',  'date' : '2026-02-06 17:00:00', 'price' : '8' }) 

    cursor execute (sql ,
        {'id_play' : '3', 'id_hall' : '1', 'date' : '2026-02-06 17:45:00', 'price' : '8' }) 


    db.commit();
    cursor.close();

    return f'seed_table_performances: OK';

#TO DO
def seed_table_halls():
    db = get_db_connection();
    cursor = db.cursor();

    sql = 'INSERT INTO rezervator_halls(id_hall, id_location, hall_capacity) VALUES (%(id_hall)s, %(id_location)s, %(capacity)s)'

    cursor.execute(sql, 
    {'id_hall' : '1' , 'capacity' : '100'})

    cursor.execute(sql, 
    {'id_hall' : '2' , 'capacity' : '80'})

    db.commit();
    cursor.close();

    return f'seed_table_halls: OK';   

#TO DO
def seed_table_locations():
    db = get_db_connection();
    cursor = db.cursor();


    sql = 'INSERT INTO rezervator.locations(name_location, address_location ) VALUES (%(name)s, %(address)s)' 

    cursor.execute(sql ,
    {'name' : 'Samobor', 'address' : 'Ulica Mate Lovraka 4'})

    db.commit();
    cursor.close();

    return f'seed_table_locations: OK';

#TO DO
def seed_table_seats():
    db = get_db_connection();
    cursor = db.cursor();

    sql = 'INSERT INTO rezervator.seats(id_hall, row_seat, column_seat) VALUES (%(id_hall)s, %(row)s, %(col)s)'

    for i in range (1,11):
        for j in range (1, 11):
            cursor.execute(sql, {'id_hall' : '1', 'row' : i, 'col' : j})

    for i in range (1,11):
        for j in range (1, 9):
            cursor.execute(sql, {'id_hall' : '2', 'row' : i, 'col' : j})
    

    db.commit();
    cursor.close();

    return f'seed_table_seats: OK';

