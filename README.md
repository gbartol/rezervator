# Rezervator

Prekopirano od profesora (zadatak6-orm), promijenjeno za projekt.


SQLAlchemy i migracije

* Za početak, stvorite **novu, praznu** bazu podatka pomoću phpmysql.
* Zatim prekopirajte example.config u app.config i prilagodite podatke za spajanje.
* Zatim u konzoli napravite početnu migraciju:
    - `flask db init`
    - `flask db migrate -m "Prva migracija"`
    - `flask db upgrade`
* Ovo bi trebalo u vašoj bazi napraviti tablice users, plays, performances, seats itd. (vidi u phpmyadmin!)
* Stupci tih tablica su točno oni koji su navedeni u klasama User, Play, Performance, Seat...!
* Pokrenite aplikaciju sa `flask run --debug`
* Posjetite rutu `/db/seed_tables/`. To bi trebalo popuniti tablice u bazi podacima (vidi u phpmyadmin!)


# Rad s migracijama u konzoli

* `flask db init` - Inicijalizira okruženje za migracije (stvara novi folder `migrations` i u njemu pripremu za migracije).
* `flask db migrate -m "poruka"` - Prvi put i nakon svake izmjene nekog modela.
* `flask db upgrade` - Da se zaista provede migracija.
* `flask db downgrade` - Za izbrisati tablice
* ili ako ih to ne izbriše napisati u PHPMyAdmin SQL konzolu: `DROP TABLE reservations, seats, performances, halls, locations, plays, users, alembic_version` (u tom redosljedu)

Kod aplikacija koje koriste migracije bismo trebali imati zasebnu bazu za svaku aplikaciju. Naime:
**Oprez:** Ako u bazi postoje neke druge tablice od prije, a modeli ih ne koriste, **migracija će ih sve obrisati**.

