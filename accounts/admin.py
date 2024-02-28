from django.contrib import admin

from accounts.models import User


@admin.register(User)
class ModelNameAdmin(admin.ModelAdmin):
    pass
