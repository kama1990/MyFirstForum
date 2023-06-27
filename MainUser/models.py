from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    picture = models.ImageField(blank=True)
    newsletterOn = models.BooleanField(default=False)
    notificationsOn = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.user.id} | {self.user.username}'
 