release: python manage.py migrate
web: daphne devtest.asgi:application --port $PORT --bind 0.0.0.0 -v2
celery: celery -A crm.celery worker --pool=solo -l info
celerybeat: celery -A crm beat -l INFO