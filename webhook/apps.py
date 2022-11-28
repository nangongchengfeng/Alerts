from django.apps import AppConfig


class WebhookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'webhook'
    verbose_name = '告警展示'
