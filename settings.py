import os
import dj_database_url

# Base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Secret Key (use environment variable in production)
SECRET_KEY = os.getenv('SECRET_KEY', None)

if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set in the environment variables.")

# Debug Mode (ensure it’s set to False in production)
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Allowed Hosts (Include your domain and Render subdomain here)
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'swifttalentforge.com,www.swifttalentforge.com').split(',')

# Installed Apps (default apps and any custom apps like 'Portal' and 'chat')
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

# Middleware (includes WhiteNoise for static file handling and security improvements)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Security middleware
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Static files handling
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Prevents clickjacking
    'django.middleware.contenttype.ContentTypeMiddleware',  # Prevents mime-sniffing attacks
]

# Root URL Configuration
ROOT_URLCONF = 'Work.urls'

# Templates Configuration
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

# Channels Configuration for Redis (if using WebSockets)
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [os.getenv('REDIS_URL', 'redis://localhost:6379')],
        },
    },
}

# ASGI and WSGI Applications (for ASGI/WSGI support)
ASGI_APPLICATION = "Work.asgi.application"
WSGI_APPLICATION = 'Work.wsgi.application'

# Database Configuration (using dj_database_url for production and SQLite as fallback)
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3'),  # Use environment variable for DB URL
        conn_max_age=600,  # Persistent connections in production
        ssl_require=True  # Ensure SSL is used in production for security
    )
}

# Authentication Backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Password Validators (Django’s default validators)
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

# Internationalization and Localization Settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static File Configuration (served by WhiteNoise in production)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media File Configuration (Use secure storage for user files if needed)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Logging Configuration (Set appropriate log level for production)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',  # Set to WARNING for production (less verbose than DEBUG)
    },
}

# Email Configuration (Use environment variables for email credentials)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True  # Use TLS for Gmail SMTP
EMAIL_USE_SSL = False
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'your-email@gmail.com')  # Your email address
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', None)  # Use environment variable for security

if not EMAIL_HOST_PASSWORD:
    raise ValueError("EMAIL_HOST_PASSWORD is not set in the environment variables.")

# Default Auto Field (Django 3.2+)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Security Configuration (ensure that Django uses HTTPS in production)
SECURE_SSL_REDIRECT = True  # Redirect HTTP to HTTPS in production
CSRF_COOKIE_SECURE = True  # Set CSRF cookie to be secure (HTTPS only)
SESSION_COOKIE_SECURE = True  # Set session cookie to be secure (HTTPS only)

# Internal Address for Communication on Render (for internal services)
INTERNAL_ADDRESS = 'swiftgen-core:10000'  # Example internal address for inter-service communication

# Security Headers (Protection against common attacks)
SECURE_BROWSER_XSS_FILTER = True
X_CONTENT_TYPE_OPTIONS = 'nosniff'
X_FRAME_OPTIONS = 'DENY'  # Prevents your site from being embedded in an iframe (clickjacking protection)

# Enable HSTS (HTTP Strict Transport Security)
SECURE_HSTS_SECONDS = 31536000  # 1 year in seconds
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply to all subdomains
SECURE_HSTS_PRELOAD = True  # Preload HSTS in browsers that support it
