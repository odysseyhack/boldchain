### Run

### Initialize database

```
cd boldapi
python manage.py create_users 2
python manage.py create_pension_funds 5
python manage.py create_entities 2
python manage.py create_giftcards 10
```

### To run admin site

```
cd boldapi
python manage.py migrate
python manage.py runserver
```
In browser, open `http://localhost:8000`
