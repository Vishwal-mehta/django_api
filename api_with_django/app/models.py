from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30) 
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='posts')
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Likes(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.name} likes {self.post.title}'
