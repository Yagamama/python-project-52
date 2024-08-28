from django.db import models

class Users(models.Model):

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150, null=False)
    password = models.CharField(max_length=150, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
