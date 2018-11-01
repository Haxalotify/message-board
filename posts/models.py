from django.db import models

# Create your models here.
#creating a model to store the textual
#content of a message board post
class Post(models.Model):
    text = models.TextField() #specifying type of content
