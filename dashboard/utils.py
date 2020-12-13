from time import timezone

from .models import hitchHikeRequest
from .serializers import hitchHikeRequestSerializers
from background_task import background
from datetime import datetime
import json

def getRequestsDataBasedOnCondition(status="", userEmail = ""):
    requestData = None
    if status:
        hitchHikeRequestRequests = hitchHikeRequest.objects.filter(status="Pending")
    elif userEmail:
        hitchHikeRequestRequests = hitchHikeRequest.objects.filter(email=userEmail)
    else:
        hitchHikeRequestRequests = hitchHikeRequest.objects.all()

    serializer = hitchHikeRequestSerializers(hitchHikeRequestRequests, many=True)
    if serializer.data:
        requestData = serializer.data

    return requestData

# def checkUserExitsOrNot(userEmail):
#     status = False
#     userLoginData = userLoginData.objects.filter(email=userEmail)
#
#     serializer =

# @background(schedule= timezone.now())
# def notify_user(requestData):
#     print("notifyUser____________________________ %s", requestData)


