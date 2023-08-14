from django.apps import AppConfig


class AppAdvertisementsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_advertisements'
    verbose_name =u'Объявления'
    default_app_config = 'app_advertisements.apps.AppAdvertisementsConfig'
