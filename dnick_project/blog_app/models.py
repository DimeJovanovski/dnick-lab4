from django.db import models
from django.contrib.auth.models import User


#############################################################################
#   Blogger
#############################################################################
class Blogger(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


#############################################################################
#   Post
#############################################################################
class Post(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(to=Blogger, on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


#############################################################################
#   File
#############################################################################
class File(models.Model):
    file = models.FileField(upload_to="files/", null=True, blank=True)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name


#############################################################################
#   Comment
#############################################################################
class Comment(models.Model):
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)         # the post the comment is in
    user = models.ForeignKey(to=Blogger, on_delete=models.CASCADE)      # the author of the comment

    def __str__(self):
        return self.content


#############################################################################
#   Block
#############################################################################
class Block(models.Model):
    blocker = models.ForeignKey(to=Blogger, on_delete=models.CASCADE, related_name="user_blocker")
    blocked = models.ForeignKey(to=Blogger, on_delete=models.CASCADE, related_name="user_blocked")

    def __str__(self):
        return str(self.blocker) + " has blocked " + str(self.blocked)

