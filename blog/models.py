from django.db import models
from django.utils import timezone
# importing User model from admin
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # we delete Post with deleted author (User) of Post

    # We define what information should be listed when calling object (Post)
    def __str__(self) -> str:
        return self.title