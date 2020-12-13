from django.urls import path
from userLogin import views


urlpatterns = [
    path('userLogin/', views.UserLogin.as_view()),


]
