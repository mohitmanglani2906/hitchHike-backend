from django.db import models
from mongoengine import *
import datetime

class userLoginData(Document):

    email = StringField(max_length=200)
    createdTime = DateTimeField()
    userEmailJson = DictField()
    authToken = StringField(max_length=300)
    idToken = StringField(min_length=10)
    loggedInWith = StringField(max_length=200)


