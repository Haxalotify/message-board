from django.db import models

# Create your models here.
#creating a model to store the textual
#content of a message board post
class Post(models.Model):
    text = models.TextField() #specifying type of content

#this function displays the first 50 characters in
#the post description
    def __str__(self):
        return self.text[:50]
