from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin





admin.site.register(
    models.CustomUser,
)  # CustomUserAdmin
admin.site.register(
    models.FuncionarioProfile
)
admin.site.register(
    models.ClienteProfile,
)
