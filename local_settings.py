import os
BASE_DIR = os.path.dirname(os.path.dirnam(os.path.abspath(__file)))

DATABASES = {
    "default":{
        'ENGINE' : "django.db.backends.sqlite3",
        "NAME"  : os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}