from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'your-secret-key'

DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # Default and custom apps
]

MIDDLEWARE = [
    # Default middleware
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        # Template settings
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'

# Database, Static, Media, Authentication, etc.
