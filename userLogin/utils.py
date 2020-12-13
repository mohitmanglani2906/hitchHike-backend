from .serializers import userLoginDataSerializers
from .models import userLoginData

def checkUserExitsOrNot(userEmail):
    userData = None
    savedUserData = userLoginData.objects.filter(email=userEmail)
    serializer = userLoginDataSerializers(savedUserData, many=True)

    if serializer.data:
        userData = serializer.data
        return True, userData

    return False, userData


# def getUserNames(userEmail):
#     print("User Email____ %s", userEmail)
#     savedUserData = userLoginData.objects.filter(email=userEmail)
#     print("Saved User Data___ %s", savedUserData)


