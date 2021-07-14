SECRET_KEY = "12345"

ALLOWED_HOSTS = ['*']

DATABASES = {}

INSTALLED_APPS = [
    "django_htmx",
    "django_htmx_extras",
]

MIDDLEWARE = []

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "OPTIONS": {"context_processors": []},
    }
]
