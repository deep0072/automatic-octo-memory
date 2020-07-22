from django.apps import AppConfig


class DummyConfig(AppConfig):
    name = 'dummy'

    def ready(self):
    	import dummy.signals
