# Simple Contact Form

### Requirements
1. Docker.

### Running the project
1. Clone the repo: 
    ```bash
    git clone https://github.com/zacniewski/simple-contact-form.git 
    cd simple-contact-form
    ```
2. `Makefile` was created to help user with running the project.
3. To initialize the project: `make docker-up`.
4. To aplly the migrations: 
    ```bash
    make make-migrations 
    make migrate
    ```
5. To create the superuser: `make create-superuser` (login: `admin`, password: `admin123`).
6. To create the non-admin user: `make create-user` (login: `testuser`, password: `test1234`).
7. To check functionalities you should log in with aforementioned credentials.
8. Fixtures `contacts.json` (40 contacts) were created. To apply them:  `make load-fixtures`
9. To run project in the browser, go to the [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### Tests
1. Tests were created with [pytest-django](https://pytest-django.readthedocs.io/en/latest/) and [pytest-drf](https://pypi.org/project/pytest-drf/).
2. All test are placed in `tests` directory.
3. To run the tests: `make test-contacts`.
4. To run `coverage`: `make run-coverage` and then `make coverage-html` to generate HTML report.
5. At this moment coverage result is 89%.

### Structure of the project
```bash
.
├── contacts
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── static
│   │   ├── css
│   │   └── js
│   ├── urls.py
│   └── views.py
├── contacts.json
├── core
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── docker-compose.yml
├── Dockerfile
├── Makefile
├── manage.py
├── pytest.ini
├── README.md
├── requirements.txt
├── templates
│   ├── base.html
│   ├── contact_list.html
│   ├── create_contact.html
│   ├── delete_contact.html
│   ├── home_page.html
│   ├── _pagination.html
│   ├── registration
│   │   ├── logged_out.html
│   │   └── login.html
│   └── update_contact.html
└── tests
    ├── conftest.py
    └── test_contacts.py

```