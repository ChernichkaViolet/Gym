from django.contrib import admin
from solo.admin import SingletonModelAdmin
from . models import SiteSettings, Profile


# Register your models here.
admin.site.register(SiteSettings, SingletonModelAdmin)
admin.site.register(Profile)