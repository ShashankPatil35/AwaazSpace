from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) #basically consider only that tweets which are assciated with user ,not considering unknown tweets
    text = models.TextField(max_length=240)#accepting max 240 characters
    photo = models.ImageField(upload_to='photos/',
                              blank=True,null=True) #this is for to tweet normal without photo
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'#The __str__ method returns a string representation of the object, showing the username and the first 10 characters of the text.
    
