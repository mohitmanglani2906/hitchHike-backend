from django.urls import path
from dashboard import views


urlpatterns = [
    path('hitchHikeRequests/', views.UserRequests.as_view()),
    path('allRequests/', views.AllRequests.as_view()),
    path('myRequests/', views.MyRequests.as_view()),
    path('getUserDetails/', views.UserDetails.as_view())

]
