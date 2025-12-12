# Terminoppgave
# Flask-prosjekt -- Dokumentasjon

## 1. Forside

**Spillanmeldelse**\
**Talha**\
**2IMI**\
**11.11.25**

**Kort beskrivelse av prosjektet:**\
*Applikasjonen går ut på å skrive anmeldelse for ulike spill. Du registrer deg og kommer deretter i en fane med ulike spill, som du kan velge. Klikk på spillet du vil gi tilbakemelding på og skriv hva du vil. Det vil også er en gjennomsnittlig vurdering av spill ved bruk av stjerner. 

------------------------------------------------------------------------

## 2. Systembeskrivelse

**Formål med applikasjonen:**\
*Jeg prøver å oppnå en applikasjon hvor folk med spillhobby kan vende til og skrive en positiv/negativ tilbakemelding. Dette kan gi ulike spillere en oppriktig mening på hva som er bra og dårlig med spillet, slik at spillere kan velge selv om de vil kjøpe spillet eller ikke. *

**Brukerflyt:**\
*Du får opp registrasjon siden hvor du oppretter en bruker. Etter å ha registrert blir du tatt til hjemsiden med alle spillene. Her vil du se ulike spill med en gjennomsnittlig vurdering. Det vil være en Legg til spill knapp som vil ta deg til en form side hvor du skriver inn informasjon om spillet. Å klikke på et av spillene på hjemsiden vil du bli tatt til en annen form side hvor du skriver din anmeldelse og gir din stjernevurdering. Her står også info om spillet. Du kan også trykke Vis anmeldelser for å se hvilke tilbakemeldinger og vurdering ulike brukere har gitt. Hver side skal inneholde en Gå til hjemside knapp slik at du kan lett navigere tilbake. *

**Teknologier brukt:**

-   Python / Flask\
-   MariaDB\ MySQL
-   HTML

------------------------------------------------------------------------

## 3. Server-, infrastruktur- og nettverksoppsett

### Servermiljø

*Ubuntu*

### Nettverksoppsett

-   Nettverksdiagram
-   IP-adresser\ 10.200.14.26
-   Porter\
-   Brannmurregler

Eksempel:

    Klient → Waitress → MariaDB

### Tjenestekonfigurasjon

-   systemctl / Supervisor\
-   Filrettigheter\
-   Miljøvariabler

------------------------------------------------------------------------

## 4. Prosjektstyring -- GitHub Projects (Kanban)

-   To Do / In Progress / Done\
-   Issues\
-   Skjermbilde (valgfritt)

Refleksjon: Hvordan hjalp Kanban arbeidet?
Kanban holdt hjalp med å holde en tydelig struktur på arbeidet og gjorde det ryddigere. Jeg visste hva jeg måtte jobbe med og hva jeg jobber på. Dette gjorde det enklere for meg å holde kontroll på hva jeg gjør.
------------------------------------------------------------------------

## 5. Databasebeskrivelse

**Databasenavn:**

**Tabeller:**\

Dette er hvordan tabellene ser ut:
+----+----------+----------------+
| id | username | password       |
+----+----------+----------------+
|  1 | talha    | Fotball2008    |
|  2 | bigt     | mypass123      |
+----+----------+----------------+

+----+---------+---------+--------+------------------------------+
| id | user_id | game_id | rating | comment                      |
+----+---------+---------+--------+------------------------------+
|  1 |   1     |   2     |   5    | Amazing game!                |
|  2 |   2     |   1     |   3    | Fun but gets repetitive.     |
+----+---------+---------+--------+------------------------------+

+----+-----------------+----------------------+----------+-------------+--------------+-------------------------------+----------------+
| id | name            | description          | genre    | developer   | release_year | cover_url                    | average_rating |
+----+-----------------+----------------------+----------+-------------+--------------+-------------------------------+----------------+
|  1 | Fortnite        | Battle royale game   | Shooter  | Epic Games  | 2017         | https://image.com/fort.png   | 4.5            |
|  2 | Minecraft       | Sandbox building     | Sandbox  | Mojang      | 2011         | https://image.com/mc.png     | 5.0            |
+----+-----------------+----------------------+----------+-------------+--------------+-------------------------------+----------------+



**SQL-eksempel:**

```
CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT,
    username VARCHAR(255),
    rating INT,
    comment TEXT,
    FOREIGN KEY (game_id) REFERENCES games(id)
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE games (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    genre VARCHAR(100) NOT NULL,
    developer VARCHAR(150) NOT NULL,
    release_year INT NOT NULL,
    cover_url TEXT,
    average_rating FLOAT DEFAULT NULL
);

```

------------------------------------------------------------------------

## 6. Programstruktur

    Terminoppgave/
     ├── .venv
     ├── app.py
     ├── templates/ 
          addgame.html
          home.html
          index.html
          login.html
          register.html
          review.html
          
Databasestrøm:

    HTML → Flask → MariaDB → Flask → HTML-tabell

------------------------------------------------------------------------

## 7. Kodeforklaring

Forklar ruter og funksjoner (kort).

@app.route("/")
dette er start siden index.html hvor du kan registrere eller logge deg inn

@app.route("/register", methods=["GET", "POST"]) 
dette er registrasjons siden om du ikke har en bruker så registrerer du deg her

@app.route("/login", methods=["GET", "POST"])
om du har en bruker så logger du inn her 

@app.route("/home")
dette er hjem siden med alle spillene. her kan du altså legge til spill, se spill som har lagt til, og gi en anmeldelse på dem.

@app.route("/addgame", methods=["GET", "POST"])
Dette er legg til spill siden hvor du skriver inn et spill og ulike ting om spillet du vil legge til.

@app.route("/game/<int:game_id>", methods=["GET", "POST"])
Dette er review siden. Her skriver du anmeldelse om spillet du valgte. 
------------------------------------------------------------------------

## 8. Sikkerhet og pålitelighet

-   .env\
-   Miljøvariabler\
-   Parameteriserte spørringer\ mycursor.execute("SELECT id FROM users WHERE username = %s", (username,))
-   Validering\ if not user:
    return render_template("login.html", error="User does not exist!")
-   Feilhåndtering 

------------------------------------------------------------------------

## 9. Feilsøking og testing

-   Typiske feil\ FIkk ofte feil at nettsiden ikke funket. Dette var fordi jeg ofte hadde blandet routesa eller skrevet en kode som overkjører programmet.
-   Hvordan du løste dem\ Jeg løste dem ved å gå over koden jeg skrev og fjerne en linje for å se hva som faktisk forårsaker problemet. Til slutt fant jeg linjen med kode og endret den. 

------------------------------------------------------------------------

## 10. Konklusjon og refleksjon

-   Hva lærte du?\ Jeg lærte veldig masse. Alt fra hvordan databaser funker til hvordan selve koden funker. Jeg har fått en mye bedre forståelse for databaser og hvordan de funker. Samtidig har jeg lært å bruke flask med html og lært meg å bruke github på en ordentlig måte.
-   Hva fungerte bra?\ Det som fungerte bra var html koden ikke hadde noe problemer og alt funket som det skulle. Jeg fikk nettsiden til å bli akkurat som jeg ville så det er jeg glad for.
-   Hva ville du gjort annerledes?\ Det jeg ville gjort annerledes er å ha jobbet mer effektivt så jeg kunne fått tid til css og style selve nettsiden.
-   Hva var utfordrende? Det som var utfordrende var html koden i flask. Det er litt annerledes enn vanlig html så det var litt krevende.

------------------------------------------------------------------------

## 11. Kildeliste

-   w3schools
-   flask.palletsprojects.com
-   Youtube
