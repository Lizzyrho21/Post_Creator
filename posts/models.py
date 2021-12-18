from django.db import models
from django.contrib.auth import get_user_model #referencing the User model when dealing with "unknown" User model.

# Create your models here.

#Create our select field choices
FEELING_CHOICES = (
    ("HAPPY", "😊"),
    ("SAD", "😔"),
    ("ANGRY", "😠"),
    ("SURPRISED", "😮"),
    ("CONFUSED", "😕"),
)

class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    emotions = models.CharField(
        max_length = 20,
        choices = FEELING_CHOICES,
        default = 'HAPPY'
        )
    body = models.TextField()
    #  auto_now_add <== This adds the time created 
    created_at = models.DateTimeField(auto_now_add=True)
    # Each time the entry is modified, it will add time modifed with auto_now!
    updated_at = models.DateTimeField(auto_now=True)

# overriding the toString() for more user friendly output
    def __str__(self):
        return self.title

