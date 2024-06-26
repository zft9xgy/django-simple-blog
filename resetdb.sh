find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

# borra base datos
# makemigrations and migrate


echo 'ejecuta el siguiente comando en la shell de python'
echo 'python manage.py shell'
echo 'exec(open('dummy-data.py').read())'


