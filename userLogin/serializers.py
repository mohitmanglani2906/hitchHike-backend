from rest_framework_mongoengine import serializers
from .models import userLoginData


class userLoginDataSerializers(serializers.DocumentSerializer):
    class Meta:
        model = userLoginData
        fields = '__all__'
