# PlayerAPI

## Vaatimukset

- Python 3.10 tai uudempi
- pip
- venv

## Asennusohjeet

Lataa projekti koneellesi

luo ja aktivoi virtuaaliympäristö
    python -m venv venv

    windows:
    venv\Scripts\activate

    mac:
    source venv/bin/activate

Asenna riippuvuudet
    pip install -r requirements.txt

Käynnistä sovellus (katso että olet sijainnissa \app)
    fastapi dev main.py

Avaa selain ja siirry osoitteeseen:
    http://127.0.0.1:8000/docs


tai paina komentokehoitteesta (ctrl + click):
    Documentation at http://127.0.0.1:8000/docs