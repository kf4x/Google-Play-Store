from django.db import models

    

class AndroidPermission(models.Model):
    """Permissions for app"""
    name = models.CharField(max_length=512)
    description = models.TextField()
    category = models.CharField(max_length=512)
    

class AndroidApplication(models.Model):
    """Listing"""
    name = models.CharField(max_length=512)
    description = models.TextField()
    package = models.CharField(max_length=512)
    category = models.CharField(max_length=512)

    # many to many 
    permissions = models.ManyToManyField(AndroidPermission, related_name='apps')

class ApplicationReview(models.Model):
    """Comments/Reivews for app"""
    user = models.CharField(max_length=512)
    text = models.TextField()

    # one to many
    app = models.ForeignKey(AndroidApplication)

class ApplicationScreenShot(models.Model):
    """Screen Shot for app"""
    location = models.CharField(max_length=512, default='')
    
    # one to many
    app = models.ForeignKey(AndroidApplication)
