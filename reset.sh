rm db.sqlite3
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput 
export DJANGO_SUPERUSER_PASSWORD='hola1234'
python manage.py createsuperuser --noinput --username jade --email jade@email.es
python populate_data.py

