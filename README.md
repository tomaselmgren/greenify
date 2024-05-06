### Köra projektet

Grundläggande kommando för att köra webbservern:
`python3 manage.py runserver`

Om den härjar om migrations:
1. `python3 manage.py makemigrations`(Ska användas efter att man har gjort ändringar i models.py)
2. `python3 manage.py migrate`

### Använda Admin Dashboard

Skapa superuser:
`python3 manage.py createsuperuser --username=xxx --email=xxx@example.com`

Sedan kör servern, och gå till localhost:8000/admin och logga in.