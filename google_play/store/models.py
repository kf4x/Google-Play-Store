from django.db import models

# Create your models here.


    
class Permission(models.Model):
    
    name = models.CharField(max_length=512)
    description = models.TextField()
    category = models.CharField(max_length=512)
    

class App(models.Model):

    name = models.CharField(max_length=512)
    description = models.TextField()
    package = models.CharField(max_length=512)
    category = models.CharField(max_length=512)

    # many to many 
    permissions = models.ManyToManyField(Permission, related_name='apps')
    
class Comment(models.Model):

    user = models.CharField(max_length=512)
    text = models.TextField()

    # one to many
    app = models.ForeignKey(App)
