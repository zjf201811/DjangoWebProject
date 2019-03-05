from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'user'
