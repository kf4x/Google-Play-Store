__author__ = 'Javier Chavez'
import logging
import json
import os
from django.core.management.base import BaseCommand
import subprocess
from optparse import make_option
from store.models import ApplicationReview, AndroidApplication, AndroidPermission, ApplicationScreenShot


class Command(BaseCommand):
    args = '<file-name ...>'

    option_list = BaseCommand.option_list + (
        make_option('--path',
                    action='store',
                    dest='path',
                    type='string',
                    default=None,
                    help='Path to which the file(s) will be imported from. --path="my/path"'
                ),
        make_option('--all',
                    action='store_true',
                    dest='imp_all',
                    default=False,
                    help='Import all apps'
                ),
    )
    def handle(self, *args, **options):
        path = options['path']
        if path is None:
            print("Using CWD as destination")
            path = os.getcwd()
            
        import_app(path)
    
    
class JSONHandler(object):
    def __init__(self):
        self.data = None

    def deserialize(self, data):
        """JSON to DB"""
        
        self.data = data
        done = None

        if isinstance(data, dict):
            done = self._odecode()
        elif isinstance(data, list):
            done = self._ldecode()
        else:
            logging.error('Deserialize failed')
            
        logging.debug('deserialize done')

        
    def _odecode(self, obj=None):
        """Add object to DB"""
        
        if obj == None:
            obj = self.data

        #keys = self.data.keys()
        app = self._application(obj)
        
        for k in obj.keys():
            if 'permission' in k:
                self._permission(app, obj[k])

            if 'screenshot' in k:
                 self._screenshot(app, obj[k])
            
        return app
                
    def _ldecode(self):
        """Add list of objects to DB"""
        tmp = 0
        for obj in self.data:
            tmp +=1
            self._odecode(obj)
        return tmp

    
    def _permission(self, app, data):
        """Assiociate app's permissions"""
        for perm in data:
            p, created = AndroidPermission.objects.get_or_create(
                name=perm)
            app.permissions.add(p)
            
            
    def _application(self, data):
        """Add application to Database"""
        app, created = AndroidApplication.objects.get_or_create(
            name=data['name'],
            package=data['package'])

        logging.debug("app %s" % app.name)

        # icon function
        icon = data['icon'].decode('unicode-escape')
        if icon[-3:] == "-rw":
            icon = icon[:-3]
            
        app.icon = icon
        # end icon fucntion

        app.rating = data['rating']
        app.total_ratings = data['total_ratings']
        app.description = data['description']
        app.pub_date = data['pub_date']
        app.price = data['price']
        app.size = data['size']
        app.installs = data['installs']
        
        app.save()
        return app
    
    def _review(self, data):
        pass

    def _screenshot(self, app, data):
        """Add screenshots and assiociate with app"""
        for ss in data:
            s, created = ApplicationScreenShot.objects.get_or_create(
                location=ss,
                app=app
            )
        
def import_app(path):
    threshhold = 250 
    fp = open(path, 'r')
    handlr = JSONHandler()
    searches = json.load(fp)
    fp.close()

    apps = []
    count = 0

    for search_term in searches.keys():
        for app in searches[search_term]:
            apps.append(app)
            if count == len(searches[search_term])-1 or count == threshhold :
                handlr.deserialize(apps)
                print 'er'
                apps = []
                count = 0
            else:
                count += 1
