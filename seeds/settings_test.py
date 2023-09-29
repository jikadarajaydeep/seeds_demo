# settings_test.py

from .settings import *  # Import settings from your main settings.py

# Database settings for testing (you can use an in-memory database or another test database)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test2_db.sqlite3',
    }
}

# Disable external services or features that you don't want to use during testing
SOME_EXTERNAL_API_ENABLED = False

# Other test-specific settings can be added here
