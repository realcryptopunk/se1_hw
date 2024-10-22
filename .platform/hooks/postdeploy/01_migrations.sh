#!/bin/bash

source /var/app/venv/*/bin/activate
cd /var/app/current

# Set permissions
touch db.sqlite3
chmod 666 db.sqlite3

# Run migrations
python manage.py migrate
python manage.py shell << END
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'password123')
END