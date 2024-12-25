## Backend for OAuth Sandbox

### Create an environment

```sh
mkdir backend
cd backend
touch README.md .gitignore
```

### Install Django via poetry

```sh
poetry init

Package name [backend]:  app
Version [0.1.0]:  
Description []:  
Author [dhythm <yuta.okada.20@gmail.com>, n to skip]:  
License []:  
Compatible Python versions [^3.9]:  ^3.10

Would you like to define your main dependencies interactively? (yes/no) [yes] 
Package to add or search for (leave blank to skip): 

Would you like to define your development dependencies interactively? (yes/no) [yes] 
Package to add or search for (leave blank to skip): 

Do you confirm generation? (yes/no) [yes]
```

```sh
poetry env use 3.10.9
poetry install --no-root
```

To get python path for poetry and update `python.defaultInterpreterPath` and `python.autoComplete.extraPaths` in `settings.json`.

```sh
poetry shell
```

```sh
poetry add Django
poetry add djangorestframework
poetry add django-cors-headers
poetry add psycopg
poetry add inertia-django
poetry add django-vite
```

```sh
poetry add --dev black isort autoflake
poetry add --dev mypy django-stubs djangorestframework-stubs
```

```sh
poetry run django-admin startproject app .
poetry run python manage.py migrate
```

### Run app

```sh
poetry run python manage.py runserver 8080
```

### Create a new django app

```sh
poetry run python manage.py startapp oauth
poetry run python manage.py makemigrations
poetry run python manage.py migrate
```