from django.db import models

class User(models.Model):

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150, null=False)
    password = models.CharField(max_length=150, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def can_edit(self, user_id):
        return self.id == user_id
    
    def __str__(self) -> str:
        return self.username
    