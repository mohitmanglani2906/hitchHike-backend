# from djongo import models
from mongoengine import *
from django.db import models
import datetime
# Create your models here.

class hitchHikeRequest(Document):

    email = StringField(max_length=200)
    sourcePlace = StringField(max_length=200)
    destinationPlace = StringField(max_length=200)
    initiatedTime = DateTimeField(default=datetime.datetime.now())
    leavingTime = DateTimeField(default=datetime.datetime.now())
    subDestinationPlaces = ListField()
    status = StringField(max_length=200)




