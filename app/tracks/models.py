from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

#helper class that allows to build database model
class Track(models.Model):
    #below are fields that will map to particular database columns
    title = models.CharField(max_length=20) #set max length of title field
    description = models.TextField(blank=True) #blank=True makes this field optional
    url = models.URLField(default='http://tracks.com') #URLField comes with validation of url
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    #note that, when track is created, an id is automatically created
    #id will serve as primary key for track

