from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

class PeaceLandConfig(AdminConfig):
    default_site = 'PeaceLand.admin.HotelAdminArea'

class PeaceLandConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "PeaceLand"
    verbose_name = "Hotel Admin"