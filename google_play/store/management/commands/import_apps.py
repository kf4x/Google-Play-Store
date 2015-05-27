__author__ = 'Javier Chavez'
import logging
import json
import os
from django.core.management.base import BaseCommand
import subprocess
from optparse import make_option
from store.models import ApplicationReview, AndroidApplication, AndroidPermission, ApplicationScreenShot, ApplicationRating


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
            return done.name
        elif isinstance(data, list):
            done = self._ldecode()
            return str(done) + " apps"
        else:
            logging.error('Deserialize failed')

        
        return "error"

        
    def _odecode(self, obj=None):
        """Add object to DB"""
        
        if obj == None:
            obj = self.data

        #keys = self.data.keys()
        app, created = self._application(obj)

        if not created:
            return app
        
        for k in obj.keys():
            if 'permission' in k:
                self._permission(app, obj[k])

            if 'screenshot' in k:
                 self._screenshot(app, obj[k])

            if 'rating' in k:
                self._rating(app, obj[k])

            if 'reviews' in k:
                self._review(app, obj[k])

                
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

        if not created:
            return app, created
        
        # icon function
        icon = data['icon'] if 'icon' in data else ''
        if icon and icon[-3:] == "-rw":
            icon = icon[:-3]
        app.icon = icon

        
        app.description = data['description'] if 'description' in data else ''
        app.pub_date = data['pub_date'] if 'pub_date' in data else ''
        app.price = data['price'] if 'price' in data else ''
        app.size = data['size'] if 'size' in data else ''
        app.installs = data['installs'] if 'installs' in data else ''
        app.developer = data['developer'] if 'developer' in data else ''
        
        app.save()
        return app, created

    def _rating(self, app, data):
        r = ApplicationRating(app = app)

        r.one_star = data['one_star']
        r.two_star = data['two_star']
        r.three_star = data['three_star']
        r.four_star = data['four_star']
        r.five_star = data['five_star']
        r.total_ratings = data['total_ratings']
        r.rating = data['rating']
        r.save()
        
    def _review(self, app, data):
        """Add review and assiociate to app"""
        for rev in data:
            s = ApplicationReview(
                user_pic = rev['image'],
                user = rev['author'],
                user_rating = rev['rating'],
                text = rev['review-text'],
                title = rev['title'],
                app = app
            )
            s.save()

    def _screenshot(self, app, data):
        """Add screenshots and assiociate with app"""
        for ss in data:
            s = ApplicationScreenShot(
                location=ss,
                app=app
            )
            s.save()
        
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
                ret = handlr.deserialize(apps)
                # logging.debug('Serialized %s' % ret) 
                apps = []
                count = 0
            else:
                count += 1
