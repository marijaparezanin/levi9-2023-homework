# API za Statistiku Košarkaša
Ovo je jednostavni API napravljen u Pythonu i Flask-u za dobijanje statistike košarkaša iz CSV datoteke. API izračunava kako tradicionalnu tako i naprednu statistiku za svakog igrača na osnovu pruženih podataka.

## Postavljanje Okruženja
Da biste postavili okruženje i pokrenuli aplikaciju, pratite ove korake:

### Zahtevi
* Python
* Flask

### Instalacija
1. Klonirajte repozitorijum:
```
git clone https://github.com/marijaparezanin/levi9-2023-homework.git
```
3. Navigirajte do direktorijuma projekta:
```
cd levi9-2023-homework
```
5. Instalirajte zavisnosti:
```
pip install Flask
```

## Izgradnja i Pokretanje
Da biste pokrenuli aplikaciju, izvršite sledeće komande:
```
python main.py
```
Aplikacija će biti dostupna na adresi http://127.0.0.1:5000/. Za testiranje sam koristila aplikaciju Postman, ali se moze korititi i web-browser.

## API Endpointi
### Dobijanje Statistike za Igrača
* Endpoint: /stats/player/<player_full_name>
* Metod: GET
* Parametri:
  * Sub <player_full_name>: Puno ime igrača za koga želite dobiti statistiku.
