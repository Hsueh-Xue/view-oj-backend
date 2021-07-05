from django.db import models
from user.models import User


# Create your models here.
class OJ(models.Model):
    name = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=1024)
    need_password = models.BooleanField(default=False)
    status = models.IntegerField(default=0)
    need_single_thread = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class OJUser(models.Model):
    oj = models.ForeignKey('OJ', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    oj_username = models.CharField(max_length=255, null=True)
    oj_password = models.CharField(max_length=255, null=True)
    oj_cookie = models.CharField(max_length=10000, null=True)
    last_success_time = models.DateTimeField(auto_now_add=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
