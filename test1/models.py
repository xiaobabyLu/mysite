from django.db import models

# Create your models here.


class UserInfo(models.Model):
    user = models.CharField(max_length=200)
    pwd = models.CharField(max_length=200)

    def __str__(self):
        return self.user
