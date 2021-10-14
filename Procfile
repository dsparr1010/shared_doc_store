echo "web: python manage.py runserver 0.0.0.0:\$PORT" > Procfile
release: python manage.py migrate
web: gunicorn shared_doc_store.wsgi --log-file -
