req:
	poetry export -f requirements.txt -o requirements.txt

run:
	poetry run python manage.py runserver

guni:
	poetry run gunicorn project.wsgi:application

get-trans:
	poetry run django-admin makemessages --ignore="static" --ignore=".env"  -l ru

run-trans:
	poetry run django-admin compilemessages

shell:
	poetry run python manage.py shell_plus --print-sql



