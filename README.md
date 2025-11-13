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
-   MariaDB\
-   HTML / CSS / JS\
-   (valgfritt) Docker / Nginx / Gunicorn / Waitress osv.

------------------------------------------------------------------------

## 3. Server-, infrastruktur- og nettverksoppsett

### Servermiljø

*F.eks.: Ubuntu VM, Docker, fysisk server.*

### Nettverksoppsett

-   Nettverksdiagram
-   IP-adresser\
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

------------------------------------------------------------------------

## 5. Databasebeskrivelse

**Databasenavn:**

**Tabeller:**\
\| Tabell \| Felt \| Datatype \| Beskrivelse \|
\|--------\|-------\|-----------\|--------------\| \| customers \| id \|
INT \| Primærnøkkel \| \| customers \| name \| VARCHAR(255) \| Navn \|
\| customers \| address \| VARCHAR(255) \| Adresse \|

**SQL-eksempel:**

``` sql
CREATE TABLE customers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  address VARCHAR(255)
);
```

------------------------------------------------------------------------

## 6. Programstruktur

    projectnavn/
     ├── app.py
     ├── templates/
     ├── static/
     └── .env

Databasestrøm:

    HTML → Flask → MariaDB → Flask → HTML-tabell

------------------------------------------------------------------------

## 7. Kodeforklaring

Forklar ruter og funksjoner (kort).

------------------------------------------------------------------------

## 8. Sikkerhet og pålitelighet

-   .env\
-   Miljøvariabler\
-   Parameteriserte spørringer\
-   Validering\
-   Feilhåndtering

------------------------------------------------------------------------

## 9. Feilsøking og testing

-   Typiske feil\
-   Hvordan du løste dem\
-   Testmetoder

------------------------------------------------------------------------

## 10. Konklusjon og refleksjon

-   Hva lærte du?\
-   Hva fungerte bra?\
-   Hva ville du gjort annerledes?\
-   Hva var utfordrende?

------------------------------------------------------------------------

## 11. Kildeliste

-   w3schools\
-   flask.palletsprojects.com
