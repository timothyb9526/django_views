import os

SECRET_KEY = 'zpy!(t+2a@^n7q1l^m*s)b9tgm8ymk*lzq3_0(+j98*++$k04k'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'app',
    'django.contrib.staticfiles',
]

MIDDLEWARE = []

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'view_practice.wsgi.application'

STATIC_URL = '/static/'
