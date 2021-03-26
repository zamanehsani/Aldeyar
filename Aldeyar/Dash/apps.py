from django.apps import AppConfig


class DashConfig(AppConfig):
    name = 'Dash'

    def ready(self):
        import Dash.signals
