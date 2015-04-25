from django.db import models
from sortedcontainers import SortedList, SortedSet, SortedDict
# not the greatest ... 
# assuming https://github.com/javierchavez/google-research
import sys
sys.path.append("../../")
from utils import compare
from django.forms.models import model_to_dict    
from django.db.models.query import *


class AndroidPermission(models.Model):
    """Permissions for app"""
    name = models.CharField(max_length=512)
    description = models.TextField(default='')
    category = models.CharField(max_length=512, default='')
    
    def to_dict(self):
        return model_to_dict(self)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
        

class AndroidApplication(models.Model):
    """Listing"""
    icon = models.CharField(max_length=512)
    
    name = models.CharField(max_length=512)
    description = models.TextField()
    package = models.CharField(max_length=512)
    category = models.CharField(max_length=512, default='')
    total_ratings = models.FloatField(default=0.0)
    rating = models.FloatField(default=0.0)
    url = models.CharField(max_length=512, default='')
    pub_date = models.CharField(max_length=128, default='')
    price = models.CharField(max_length=128, default='')
    size = models.CharField(max_length=64,default='')
    developer = models.CharField(max_length=128, default='')
    installs = models.CharField(max_length=128, default='')
    category = models.CharField(max_length=128, default='')
    
    # many to many 
    permissions = models.ManyToManyField(AndroidPermission, related_name='apps')

    def to_dict(self):
        return model_to_dict(self, exclude='permissions')
        
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

# would like to turn into json encode
class HammingPrepare(object):
    def __init__(self):
        self.data = None

    def serialize(self, data):
        
        self.data = data
        if isinstance(data, QuerySet):
            return self._QSencode()

        
    def _app_encode(self, data):
        app = data.to_dict()
        perms = [ str(perm) for perm in data.permissions.all() ]
        app['permissions'] = perms if len(perms) > 0 else []
        return app
    
    # we can make this more generic later
    def _QSencode(self):
        apps = []
        for obj in self.data:
            app = self._app_encode(obj)
            apps.append(app)
        return apps

# getting stats of search.
def hamming_stats(apps):
    if apps == None or len(apps) == 0:
        return {"distance": 0, "stats": {}}
        
    apps = HammingPrepare().serialize(apps)
    ss = SortedSet([p.name for p in AndroidPermission.objects.all()])
    hamming = compare.Hamming(tnp=ss, key='permissions')
    transd = hamming.bin_transform(apps)
    dist = hamming.hamming_dist(transd, None)
    stats = hamming.map_names(hamming.sums(transd))
    return {
        "distance": dist,
        "stats": stats
        }
        
    
