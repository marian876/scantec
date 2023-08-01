from django.apps import AppConfig

class SeguridadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'seguridad'
    verbose_name = 'perfiles'

    def ready(self):
        import seguridad.signals