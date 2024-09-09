rungun:
	python -m gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker

run:
	python manage.py runserver

mes_en:
	django-admin makemessages --ignore=".venv" -l en_US

mes_compile:
	django-admin compilemessages

mig:
	python manage.py makemigrations
	python manage.py migrate

test: 
	python manage.py test --verbosity 2
	