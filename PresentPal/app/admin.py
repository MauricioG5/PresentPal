from django.contrib import admin

from .models import User, Auth, Gift

admin.site.register(User)
admin.site.register(Auth)
admin.site.register(Gift)
