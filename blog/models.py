from django.db import connection
import psycopg2
from collections import OrderedDict
import pprint
import sys
import csv
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class PointsTable(models.Model):
    index = models.TextField(primary_key=True)
    # Field name made lowercase.
    mat = models.BigIntegerField(db_column='Mat', blank=True, null=True)
    # Field name made lowercase.
    won = models.BigIntegerField(db_column='Won', blank=True, null=True)
    # Field name made lowercase.
    lost = models.BigIntegerField(db_column='Lost', blank=True, null=True)
    # Field name made lowercase.
    tied = models.BigIntegerField(db_column='Tied', blank=True, null=True)
    nr = models.BigIntegerField(db_column='NR', blank=True, null=True)  # Field name made lowercase.
    pts = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Points_table'
