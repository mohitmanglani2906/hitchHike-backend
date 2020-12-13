from rest_framework_mongoengine import serializers
from .models import hitchHikeRequest

# class userRequestSerializers(serializers.DocumentSerializer):
#     class Meta:
#         model = userRequest
#         fields = '__all__'

class hitchHikeRequestSerializers(serializers.DocumentSerializer):
    class Meta:
        model = hitchHikeRequest
        fields = '__all__'
