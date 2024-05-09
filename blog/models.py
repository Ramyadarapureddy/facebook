from django.db import models

# Create your models here.
from auth_manager.models import CustomUser

class Post(models.Model):
    author = models.ForeignKey(CustomUser, 
                               on_delete=models.CASCADE)
    title = models.TextField()
    image = models.ImageField(upload_to='posts/images/',
                              blank=True,null=True)
    likes = models.ManyToManyField(CustomUser, related_name="my_liked_post")
    posted_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(CustomUser,related_name="my_comments",on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    text = models.TextField()
    commeted_at = models.DateTimeField(auto_now_add=True)