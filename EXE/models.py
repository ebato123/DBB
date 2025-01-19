from django.db import models

# Create your models here.
class Comment(models.Model):
    user_name =  models.CharField(max_length=30)
    tittle = models.CharField(max_length=100)
    text = models.TextField()
    
    def __str__(self):
        return self.user_name
    
