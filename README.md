### Köra projektet

#### Steg 1: Fixa postgres

1. Ladda ner postgres lokalt om det redan inte finns
2. Kör kommandot `psql postgres` för att komma åt command line interfacet. (Det kan behövas att man skriver `psql postgres -U postgres` för att ansluta med standard användarnamnet "postgres")
3. Kör kommandot `CREATE DATABASE greenify;`
4. Kör kommandot `CREATE USER pvk-user` (detta är vad som används i settings.py just nu)
5. Kör därefter alla Migrate kommandon här nedan för att skapa alla tables i databasen!
6. Därefter kan ni i postgres skriva `\c greenify`, och sedan köra SQL queriet som finns här i greenify/sql/hea01.sql för att lägga in några exempelfrågor i databasen.

#### Steg 2: Köra programmet

Grundläggande kommando för att köra webbservern:
`python3 manage.py runserver`

Om den härjar om migrations:
1. `python3 manage.py makemigrations`(Ska användas efter att man har gjort ändringar i models.py)
2. `python3 manage.py migrate`

### Använda Admin Dashboard

Skapa superuser:
`python3 manage.py createsuperuser --username=xxx --email=xxx@example.com`

Sedan kör servern, och gå till localhost:8000/admin och logga in.