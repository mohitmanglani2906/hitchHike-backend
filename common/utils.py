from userLogin.models import userLoginData
from userLogin.serializers import userLoginDataSerializers
import json

def getUserNames(userEmail):
    userData = None
    fullName = ""
    savedUserData = userLoginData.objects.filter(email=userEmail)
    serializer = userLoginDataSerializers(savedUserData, many=True)
    if serializer.data:
        userData = serializer.data
        for uData in userData:
            if "userEmailJson" in uData and uData["userEmailJson"]:
                if "Ad" in uData["userEmailJson"] and uData["userEmailJson"]["Ad"]:
                    fullName = uData["userEmailJson"]["Ad"]
                elif "gV" in uData["userEmailJson"] and uData["userEmailJson"]["gV"]:
                    if "jT" in uData["userEmailJson"] and uData["userEmailJson"]["jT"]:
                        fullName = uData["userEmailJson"]["gV"] + " " + uData["userEmailJson"]["jT"]
                    else:
                        fullName = uData["userEmailJson"]["gV"]

    return fullName


