from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    portfolio = models.CharField(max_length=1024, blank=True)
    # profile_pic = models.ImageField(upload_to='level_five/profile_pics', blank=True)

    def __str__(self):
        return self.user.username
