
# Budget Accounting App



## Introduction

It's an application that is used to account budgets.

## Run Locally


Make fork of repository & go to the project directory

```bash
  cd my-project
```

Clone the project

```bash
  git clone https://github.com/<name_of_your_Github_profile>/Budget_Accounting_App.git
```

Cofigure PostgreSQL database in settings

```bash
  DATABASES = {
    'default': {
        'HOST': '127.0.0.1',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<name_of_database>',
        'USER': '<username>',
        'PASSWORD': '<password_to_database>',
    }
}
```

Do migrates to database

```bash
  python manage.py migrate

```

Install dependencies

```bash
  pip install -r requirements.txt

```

Start the server

```bash
    python manage.py runserver
```


## Running Tests

To run tests, run the following command

```bash
  pytest -v
```


## Roadmap

- Optimalization models (delete Category)

- Additional information about budget overruns

- View data on the charts

- Add mobile view



## Lessons Learned

- I shoud better plan models and views

- I shoud make a To-Do list with tasks

- I shuld give the app to manual tests with real users

## 🛠 Technology

- Python

- Django 

- PostgreSQL

- HTML

- Bootstrap


# Hi, I'm Mathhew! 👋

It's my first Python & Django project. If you have advice, text to me!