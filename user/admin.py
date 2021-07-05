from django.contrib import admin
from user.models import User
from oj.models import OJUser, OJ

# Register your models here.
admin.site.register(User)
admin.site.register(OJUser)
admin.site.register(OJ)
