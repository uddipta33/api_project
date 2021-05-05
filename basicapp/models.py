from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.CharField(max_length=100)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    