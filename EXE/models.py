from django.utils.timezone import localtime
from django.db import models

# Create your models here.
class Comment(models.Model):
    user_name =  models.CharField(max_length=30)
    tittle = models.CharField(max_length=100, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user_name} {self.tittle} - {self.created_at}"

