from django.apps import AppConfig


class SourceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'source'
    verbose_name = 'БД платежных карт'
