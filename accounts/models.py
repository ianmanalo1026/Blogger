from django.db import models
from django.contrib.auth.models import User




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    joined = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to="photo", default="default.jpg")
    
    def __str__(self):
        return self.user.first_name
