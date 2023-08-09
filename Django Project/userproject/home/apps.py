from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

from django.apps import AppConfig
from django.conf import settings
from pathlib import Path

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

STATICFILES_DIRS = [
    settings.BASE_DIR / "static",
]
