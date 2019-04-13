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


### API

1. [GET] /giftcards/valid
  - query_params: barcode
  - example: 127.0.0.1:8000/giftcards/valid?barcode=xyz
  - response:
  ```
  {
    "barcode": "xyz",
    "amount": 150
  }
  ```

  - example: 127.0.0.1:8000/giftcards/valid?barcode=INVALID_BARCODE
  - response:
  ```
  {
    "msg": "Invalid barcode"
  }
  ```

2. [POST] /mockdigid/authenticate
  - query_params: username, password
  - example: 127.0.0.1:8000/mockdigid/authenticate?username=test&password=root
  - response:
  ```
  {
    "first_name": "first1",
    "last_name": "last1",
    "bio": "Some bio"
  }
  ```

  - example: 127.0.0.1:8000/mockdigid/authenticate?username=INVALID&password=INVALID
  - response:
  ```
  {
    "msg": "Username or password is wrong"
  }
  ```

3. [PUT] /mockdigid/addtofund
  - query_params: barcode, id
  - example: 127.0.0.1:8000/mockdigid/addtofund?barcode=valid_barcode&id=valid_id
  - response:
  ```
  {
      "amount": 225,
      "msg": "Amount added to pension fund"
  }
  ```

  - example: 127.0.0.1:8000/mockdigid/addtofund?barcode=INVALID&id=valid_id
  - response:
  ```
  {
      "msg": "Invalid barcode"
  }
  ```

  - example: 127.0.0.1:8000/mockdigid/addtofund?barcode=valid_barcode&id=INVALID
  - response:
  ```
  {
      "msg": "Invalid Pension Fund"
  }
  ```

  - example: used giftcard
  - response
  ```
  {
      "msg": "Giftcard already used"
  }
  ```
