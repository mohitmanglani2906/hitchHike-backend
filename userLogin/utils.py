from .serializers import userLoginDataSerializers
from .models import userLoginData
import sendgrid

def checkUserExitsOrNot(userEmail):
    userData = None
    savedUserData = userLoginData.objects.filter(email=userEmail)
    serializer = userLoginDataSerializers(savedUserData, many=True)

    if serializer.data:
        userData = serializer.data
        return True, userData

    return False, userData

def sendMail(toEmail):
    send_grid = sendgrid.SendGridAPIClient(api_key="")
    data = get_data(toEmail)
    send_grid.client.mail.send.post(request_body=data)

def get_data(to_email):
   personalizations = [
    {
      "to": [
        {
          "email": to_email
        }
      ],
      "subject": "Your Account is created. Login to explore more!"
    },
    {
       "to": [
           {
               "email": "mohitmanglani2906@gmail.com"
           }
       ],
        "subject": "New user has created account " + to_email
       },
   ]
   return {
      "personalizations": personalizations,
      "from": {"email": "mohitmanglani2906@gmail.com", "name": "hitchHike"},
      "content": [{"type": "text/html", "value": "Your account is create. Please login to " + "https://hitchhike-ride.herokuapp.com/" + " to explore more."}]
   }

# def getUserNames(userEmail):
#     print("User Email____ %s", userEmail)
#     savedUserData = userLoginData.objects.filter(email=userEmail)
#     print("Saved User Data___ %s", savedUserData)


