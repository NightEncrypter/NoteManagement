from django.db import models

# Create your models here.
class Comment(models.Model):
    content=models.TextField()
    email=models.EmailField()
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.email
    