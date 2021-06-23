from django.contrib import admin
from.models import*
from home.models import Account, tsm
# Register your models here.

admin.site.register(tsm)

admin.site.register(Account)

admin.register(UserDetail)
admin.register(Account)