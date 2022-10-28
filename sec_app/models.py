from django.db import models

# Create your models here.


class Users(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=265, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}, EMail: {self.email}'
