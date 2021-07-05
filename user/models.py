from django.db import models


# Create your models here.
class User(models.Model):
    nickname = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
    codeforces_rating = models.IntegerField(default=0)
    contest_num = models.IntegerField(default=0)
    last_cf_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
