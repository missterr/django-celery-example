import os
from django_celery_example.celery import app
from celery.schedules import crontab
from kombu import Queue, Exchange

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '920uj-(g1&d%yaw_m=^hnvdzdhw1lj))d#elg4!lckld+jgf^n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_example',
    'django_celery_results',
    'django_celery_beat'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_celery_example.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_celery_example.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
# Celery

CELERY_BROKER_URL = 'redis://localhost:6379/3'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_RESULT_EXPIRES = 3 * 86400  # 3 days
CELERY_SEND_EVENTS = True
CELERY_DISABLE_RATE_LIMITS = False
HIGH_CELERY_QUEUE = 'high_development'
LOW_CELERY_QUEUE = 'low_development'

CELERY_MAIN_QUEUE = LOW_CELERY_QUEUE

app.conf.accept_content = ['application/x-python-serialize', 'pickle', 'json']
app.conf.task_serializer = 'pickle'

app.conf.beat_schedule = {
    'test': {
        'task': 'django_celery_example.tasks.test',
        'schedule': crontab()
    }
}

CELERY_TASK_ALWAYS_EAGER = False
CELERY_TASK_DEFAULT_QUEUE = CELERY_TASK_DEFAULT_EXCHANGE = CELERY_TASK_DEFAULT_ROUTING_KEY = LOW_CELERY_QUEUE

CELERY_TASK_QUEUES = (
    Queue(LOW_CELERY_QUEUE, exchange=Exchange(LOW_CELERY_QUEUE, type='direct'), routing_key=LOW_CELERY_QUEUE),
    Queue(HIGH_CELERY_QUEUE, exchange=Exchange(HIGH_CELERY_QUEUE, type='direct'), routing_key=HIGH_CELERY_QUEUE)
)

# end Celery
