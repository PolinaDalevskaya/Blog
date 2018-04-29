from django.db import models
from django.db import models
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    


    def __str__(self):
        return self.author.username+self.text[:20]