SHELL := /bin/sh
PYTHON_BIN := $(VIRTUAL_ENV)/bin

startproject:
	$(PYTHON_BIN)/django-admin startproject config .

run:
	$(PYTHON_BIN)/python manage.py runserver

makemigrations:
	$(PYTHON_BIN)/python manage.py makemigrations

migrate:
	$(PYTHON_BIN)/python manage.py migrate

shell:
	$(PYTHON_BIN)/python manage.py shell_plus

pep8:
	$(PYTHON_BIN)/flake8 --config=.flake8 apps

createsuperuser:
	$(PYTHON_BIN)/python manage.py createsuperuser --username='admin' --email='john@example.com'

translate:
	$(PYTHON_BIN)/python manage.py makemessages -l ru
