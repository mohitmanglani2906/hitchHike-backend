from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import userLoginDataSerializers
from .utils import checkUserExitsOrNot, sendMail

# Create your views here.

class UserLogin(APIView):

    # def get(self, request):
    #     print("__get log in__")
    #     userEmail = request.GET.get("userEmail")
    #     status, userData = checkUserExitsOrNot(userEmail)
    #     if not status:
    #         return Response({"success":False, "message":"Email id Not Found. Please Sign Up First!"})
    #     if not userData:
    #         return Response({"success":False, "message":"No Data Found"})
    #     print("status %s userData %s", status, userData)
    #     return Response({"success":True, "requestData":userData})
    #
    #
    # def post(self, request):
    #     print("__ post log in__")
    #     serializerUserLogIn = userLoginDataSerializers(data = request.data, context={'request': request})
    #     success = False
    #     print("request__Data___ %s", request.data)
    #     if "email" in request.data and request.data["email"]:
    #         status, userData = checkUserExitsOrNot(request.data["email"])
    #         if status and userData:
    #             return Response({"success": success, "message": "Your Email id already exists!!"})
    #     if serializerUserLogIn.is_valid():
    #         serializerUserLogIn.save()
    #         print("__serializerUserLogin__ %s", serializerUserLogIn.data)
    #         success = True
    #         return Response({"success": success, "requestData": serializerUserLogIn.data})
    #     # else:
    #     #     print("__serializerUserLogin__ %s", serializerUserLogIn.data["userEmailJson"])
    #     #     print("__Errors__ %s", serializerUserLogIn.errors)
    #     #     return Response({"success": success, "message": "Account not created. Please try again!"})
    #
    #     return Response({"success": success, "message": "Account not created. Please try again!"})

    def post(self,request):

        if "flag" in request.data and request.data["flag"]:
            print("Flag Found")
            if request.data["flag"] == "Sign Up":
                print("__ post log in__")
                serializerUserLogIn = userLoginDataSerializers(data=request.data, context={'request': request})
                success = False
                print("request__Data___ %s", request.data)
                if "email" in request.data and request.data["email"]:
                    status, userData = checkUserExitsOrNot(request.data["email"])
                    if status and userData:
                        return Response({"success": success, "message": "Your Email id already exists!!"})
                if serializerUserLogIn.is_valid():
                    serializerUserLogIn.save()
                    print("__serializerUserLogin__ %s", serializerUserLogIn.data)
                    try:
                        sendMail(serializerUserLogIn.data["email"])
                    except Exception as e:
                        print(e.message)
                    success = True
                    return Response({"success": success, "requestData": serializerUserLogIn.data})
                # else:
                #     print("__serializerUserLogin__ %s", serializerUserLogIn.data["userEmailJson"])
                #     print("__Errors__ %s", serializerUserLogIn.errors)
                #     return Response({"success": success, "message": "Account not created. Please try again!"})

                return Response({"success": success, "message": "Account not created. Please try again!"})
            elif request.data["flag"] == "Log In":
                print("__post log in__ %s", request.data["flag"])
                userEmail = request.data["userEmail"]
                status, userData = checkUserExitsOrNot(userEmail)
                if not status:
                    return Response({"success": False, "message": "Email id Not Found. Please Sign Up First!"})
                if not userData:
                    return Response({"success": False, "message": "No Data Found"})
                import json
                print("status %s userData %s", status, json.dumps(userData))
                return Response({"success": True, "requestData": userData})
        else:
            print("Flag Not Found")

#No Use
class CheckUserExists(APIView):

    def get(self, request):
        print("__ user exists or not__")
        userEmail = self.request.get("userEmail")



