from django.db import models
from user.models import User
import django.utils.timezone as timezone


# Create your models here.
class OJ(models.Model):
    name = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=1024, null=True)
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
    oj_rating = models.IntegerField(default=0)
    problem_count = models.IntegerField(default=0)
    last_login = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
