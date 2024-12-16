# settings.py
from pathlib import Path # Used to manage file paths easily
from datetime import timedelta # Used to define time intervals for JWT tokens


# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key for encryption and security (Keep it private!)
SECRET_KEY = 'your-secret-key'

# Debug mode should be turned off in production
DEBUG = True

# List of allowed hosts for the server
ALLOWED_HOSTS = ['127.0.0.1', '10.0.2.2', '192.168.41.113']

#Installed apps for the project, including built-in and third-party apps
INSTALLED_APPS = [
    'django.contrib.admin',  # Admin interface
    'django.contrib.auth',  # Authentication system
    'django.contrib.contenttypes',  # Content type framework
    'django.contrib.sessions',  # Session framework
    'django.contrib.messages',  # Messaging framework
    'django.contrib.staticfiles',  # Static file handling
    'rest_framework',  # Django REST framework
    'corsheaders',  # To handle Cross-Origin Resource Sharing (CORS)
    'social_django',  # For social authentication
    'rest_framework_simplejwt.token_blacklist',  # JWT token blacklisting
]

# Middleware components to process requests/responses
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Security enhancements
    'django.contrib.sessions.middleware.SessionMiddleware',  # Session support
    'corsheaders.middleware.CorsMiddleware',  # Add headers for CORS
    'django.middleware.common.CommonMiddleware',  # Common middleware features
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Auth support
    'django.contrib.messages.middleware.MessageMiddleware',  # Message framework
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Prevent clickjacking
    'social_django.middleware.SocialAuthExceptionMiddleware',  # Handle social auth exceptions
]

# Main URLs file for the project
ROOT_URLCONF = 'myproject3.urls'

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',# Template engine
        'DIRS': [], # Directories for custom templates
        'APP_DIRS': True,# Look for templates in app directories
        'OPTIONS': {
            'context_processors': [ # Add variables to templates
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends', # Social auth support
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

# WSGI application entry point
WSGI_APPLICATION = 'myproject3.wsgi.application'

# Database configuration (SQLite in this case)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Database engine
        'NAME': BASE_DIR / 'db.sqlite3', # Path to database file
    }
}

# Password validation rules for user authentication
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

# Language and time zone settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True # Internationalization support
USE_L10N = True # Format localization support
USE_TZ = True # Time zone support

# Static files settings
STATIC_URL = '/static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django REST Framework configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # Use JWT for authentication
    ],
}

# JWT settings for tokens
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}

# CORS (Cross-Origin Resource Sharing) settings
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000', 
    'exp://192.168.41.113:8081',  #This url will be changed as EXPO url
    'http://192.168.1.100',  
]
CORS_ALLOW_CREDENTIALS = True

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'your-google-oauth2-key'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'your-google-oauth2-secret'
SOCIAL_AUTH_REDIRECT_URI = 'http://127.0.0.1:8000/complete/google-oauth2/'
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'openid',
    'profile',
    'email'
]

# Authentication backends for user authentication
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',  Default authentication backend
)

# URLs for login/logout redirection
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '127.0.0.1' # Redirect after successful login




