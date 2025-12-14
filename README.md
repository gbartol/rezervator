# Rezervator

* Prekopirano od profesora (zadatak6-orm), upute su iste i za napraviti baze za projekt.



Ovaj folder sadrži rješenje Zadatka 6 korištenjem SQLAlchemy i migracija.

* Za početak, stvorite **novu, praznu** bazu podatka pomoću phpmysql.
* Zatim prekopirajte example.config u app.config i prilagodite podatke za spajanje.
* Zatim u konzoli napravite početnu migraciju:
    - `flask db init`
    - `flask db migrate -m "Prva migracija"
    - `flask db upgrade`
* Ovo bi trebalo u vašoj bazi napraviti tablice library_users, library_books, library_loans (vidi u phpmyadmin!)
* Stupci tih tablica su točno oni koji su navedeni u klasama User, Book, Loan!
* Pokrenite aplikaciju sa `flask run --debug`
* Posjetite rutu `/db/seed_tables/`. To bi trebalo popuniti tablice u bazi podacima (vidi u phpmyadmin!)
* Sada rade i ostale rute poput `/users/`, `/books` i slično.
* Pokušajte promijeniti model tako da npr dodate neki stupac, te napravite migraciju.


# Rad s migracijama u konzoli

* `flask db init` - Inicijalizira okruženje za migracije (stvara novi folder `migrations` i u njemu pripremu za migracije).
* `flask db migrate -m "poruka"` - Prvi put i nakon svake izmjene nekog modela.
* `flask db upgrade` - Da se zaista provede migracija.

Kod aplikacija koje koriste migracije bismo trebali imati zasebnu bazu za svaku aplikaciju. Naime:
**Oprez:** Ako u bazi postoje neke druge tablice od prije, a modeli ih ne koriste, **migracija će ih sve obrisati**.

Ako želimo to izbjeći i ipak koristiti jednu bazu za više aplikacija, onda bismo nakon `flask db init` trebali editirati `migrations/env.py` i unutar funkcije `run_migrations_online` promijeniti `context.configure()` ovako:

```
context.configure(
    ...
    version_table='alembic_version_appname', # appname=ime naše aplikacije
    include_object=include_only_my_tables,
)
```

te dodajemo funkciju

```
def include_only_my_tables(obj, name, type_, reflected, compare_to):
    # Only include tables starting with your prefix
    if( type_ == 'table' ):
        return name.startswith( 'appname_' ); # appname=ime naše aplikacije
    return True
```

Sada će migracije djelovati samo na tablice čije ime počinje sa `appname_`.
