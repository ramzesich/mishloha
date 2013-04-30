import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('dmitriy', 'ramzesich@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'adventure_works',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Asia/Jerusalem'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = False
USE_TZ = True

ROOT = os.path.realpath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(ROOT, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(ROOT, 'static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'k-p#yy$q^#i!gx2a^q0m!6=dq4cj3k-)uv)5o4z#jov2mx+#p2'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_DIRS = (
    os.path.join(ROOT, 'templates'),
)

ROOT_URLCONF = 'mishloha.urls'
WSGI_APPLICATION = 'mishloha.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'main',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
