from django.apps import AppConfig  # base class for Django app config

class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"  # app label