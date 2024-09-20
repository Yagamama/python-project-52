from django.db import models
from ..statuses.models import Status
from ..users.models import User

class Task(models.Model):

    name = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author')
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    executor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='executor')
    tag = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def can_delete(self, user_id):
        return self.id == user_id
    
    def __str__(self) -> str:
        return self.name
    