import os
import dj_database_url
import environ

# Initialize environment variables using django-environ
env = environ.Env(
    DEBUG=(bool, False),
    DJANGO_SECRET_KEY=(str, 'fallback-secret-key'),
    DB_NAME=(str, 'your-db-name'),
    DB_USER=(str, 'your-db-user'),
    DB_PASSWORD=(str, 'your-db-password'),
    DB_HOST=(str, 'localhost'),
    DB_PORT=(str, '5432'),
    REDIS_URL=(str, 'redis://localhost:6379/0'),
    EMAIL_HOST_USER=(str, 'your-email@gmail.com'),
    EMAIL_HOST_PASSWORD=(str, 'your-email-password'),
)
environ.Env.read_env()  # Reading .env file for local development

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('False')

ALLOWED_HOSTS = [
    'swiftgen-core.onrender.com',  # Render hostname
    '127.0.0.1',  # Localhost
    'swifttalentforge.com',  # Squarespace custom domain
    'www.swifttalentforge.com',  # Custom domain with www
]

# Application definition
INSTALLED_APPS = [
    'Portal',
    'chat',
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
]

# Configure Channels to use Redis as the channel layer
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [env('rediss://red-cu2r11lumphs73avnm60:8UMaKfWhFuPfs7JqdDCKpIbro89gt6Uv@oregon-redis.render.com:6379')],  # Using Redis URL from environment variable
        },
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Static files handling in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Work.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'Portal/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

ASGI_APPLICATION = "Work.asgi.application"
WSGI_APPLICATION = 'Work.wsgi.application'

# Replace SQLite database configuration with PostgreSQL
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://swiftproject_db_user:5jCqr6TucKgzmIX1ESI9juYtvTHnyInM@dpg-cu2pnapopnds73clvib0-a.oregon-postgres.render.com/swiftproject_db',
        conn_max_age=600,  # Keep persistent database connections
        ssl_require=True,   # Ensure SSL connection for security
    )
}
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Directory for static files during development
]
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Directory for collected static files in production

# Whitenoise storage configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Logging configuration (capture warnings and errors in production)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': os.environ.get('DJANGO_LOG_LEVEL', 'WARNING'),
    },
}

# Authentication backend (use default model backend)
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email backend configuration (use Gmail SMTP with environment variables)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('upworkstud198@gmail.com')  # Use environment variable
EMAIL_HOST_PASSWORD = env('yktr gjti qvhj nvci')  # Use environment variable
DEFAULT_FROM_EMAIL = 'Swift Talent Forge <info@swifttalentforge.com>'

# CSRF and Session security (enable secure cookies in production)
CSRF_TRUSTED_ORIGINS = [
    'https://swifttalentforge.com',
    'https://www.swifttalentforge.com',
    'https://swiftgen-core.onrender.com'  # Added Render domain
]

# Secure session and CSRF cookies over HTTPS
SESSION_COOKIE_SECURE = True  # Ensures session cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True     # Ensures CSRF cookies are only sent over HTTPS
