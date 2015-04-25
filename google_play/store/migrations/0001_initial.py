# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AndroidApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('icon', models.CharField(max_length=512)),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('package', models.CharField(max_length=512)),
                ('total_ratings', models.FloatField(default=0.0)),
                ('rating', models.FloatField(default=0.0)),
                ('url', models.CharField(default=b'', max_length=512)),
                ('pub_date', models.CharField(default=b'', max_length=128)),
                ('price', models.CharField(default=b'', max_length=128)),
                ('size', models.CharField(default=b'', max_length=64)),
                ('developer', models.CharField(default=b'', max_length=128)),
                ('installs', models.CharField(default=b'', max_length=128)),
                ('category', models.CharField(default=b'', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='AndroidPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField(default=b'')),
                ('category', models.CharField(default=b'', max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=512)),
                ('text', models.TextField()),
                ('app', models.ForeignKey(to='store.AndroidApplication')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationScreenShot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(default=b'', max_length=512)),
                ('app', models.ForeignKey(to='store.AndroidApplication')),
            ],
        ),
        migrations.AddField(
            model_name='androidapplication',
            name='permissions',
            field=models.ManyToManyField(related_name='apps', to='store.AndroidPermission'),
        ),
    ]
