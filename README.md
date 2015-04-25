#Google Play Store

This is a redesign of the google play store

##Running

Intstall the python requirements

```bash
pip install -r requirements.txt
```

Create your db

```bash
python manage.py syncdb
python manage.py makemigrations # may or may-not need it
python manage.py migrate
```

Run the server

```bash
python manage.py runserver
```

##Import

Make sure you change your path...

```bash
python manage.py import_apps --path="../../datasets/2k13_all_by_term.json"
```


##About
I am assisting [Dr. Kelley](http://patrickgagekelley.com/) with this research. The topic of the research is Android permissions.
The goal is to help Android users make better(safer) choices when choosing to install a Android application by carefully presenting useful
information about that apps permissions.

We want to show the user that there is no reason a wallpaper app should need permission to access phone calls by giving a graphic of average
permissions for that search.OB
