from django.apps import AppConfig


class MovietriggerappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MovieTriggerApp'
    
    def ready(self) -> None:
        import MovieTriggerApp.signals
