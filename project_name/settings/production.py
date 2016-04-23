__author__ = 'pitaside'

from base import *
DEBUG = False

#allow only our domain to access the application
ALLOWED_HOSTS = ["*"]


DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME' : '{{project_name}}',
        'USER' : 'postgres',
        'PASSWORD' : 'postgres_db_password',
        'HOST' : 'localhost',
        'PORT' : 5432
    }
}