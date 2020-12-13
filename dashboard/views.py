from django.shortcuts import render
# from rest_framework_mongoengine import *

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import hitchHikeRequest
from .serializers import hitchHikeRequestSerializers
from .utils import getRequestsDataBasedOnCondition
from common.utils import getUserNames
from userLogin.utils import checkUserExitsOrNot


class UserRequests(APIView):
    
    def get(self, request):
        requestData = None
        # userEmail = request.GET.get("userEmail")
        requestData = getRequestsDataBasedOnCondition()
        fullName = ""
        if not requestData:
            return Response({"success":False, "requestData":"No data found"})
        for request in requestData:
            if "email" in request and request["email"]:
                print("Email__ %s", request["email"])
                fullName = getUserNames(request["email"])
                request["fullName"] = fullName

        return Response({"success": True, "requestData": requestData})

    def post(self,request):
        serializerHitchHike = hitchHikeRequestSerializers(data=request.data, context={'request': request})
        success = False

        if serializerHitchHike.is_valid():
            serializerHitchHike.save()
            print("__serializerHitchHike__ %s", serializerHitchHike.data)
            success = True
            return Response({"success": success})

        return Response({"success": False})

    def put(self, request):
        print("Put___ %s, %s", request.data["id"], request.data["status"])
        requestObject = hitchHikeRequest.objects.get(id=request.data["id"])
        serializerHitchHike = hitchHikeRequestSerializers(instance=requestObject ,data=request.data)
        import json
        # print("RequestObject___ %s", json.loads(requestObject))
        if serializerHitchHike.is_valid():
            serializerHitchHike.save()
            print("data %s", serializerHitchHike.data)
            return Response({"success": True, "requestData": serializerHitchHike.data})
        else:
            print("Error___ %s", serializerHitchHike.errors)
            return Response({"success": False, "message":"No data found"})

#No Use
class AllRequests(APIView):

    def get(self, request):
        requestData = None
        requestData  = getRequestsDataBasedOnCondition("Pending")
        # notify_user(requestData)
        if not requestData:
            return Response({"success": False, "requestData": "No data found"})
        return Response({"success": True, "requestData": requestData})


class MyRequests(APIView):

    def get(self, request):
        requestData = None
        userEmail = request.GET.get("userEmail")
        print("User Email___ %s", userEmail)
        requestData = getRequestsDataBasedOnCondition(userEmail = userEmail)
        if not requestData:
            return Response({"success": False, "requestData": "No data found"})
        return Response({"success": True, "requestData": requestData})

class UserDetails(APIView):

    def get(self, request):
        # print("__Request___ %s", request["userEmail"])
        userEmail = request.GET.get("userEmail")
        status, userData = checkUserExitsOrNot(userEmail)

        if not status:
            return Response({"success": False, "message": "Email id Not Found. Please Sign Up First!"})
        if not userData:
            return Response({"success": False, "message": "No Data Found"})
        import json
        print("UserData___ %s", json.dumps(userData[0]["userEmailJson"]))
        return Response({"success": True, "userData": userData[0]["userEmailJson"]})




