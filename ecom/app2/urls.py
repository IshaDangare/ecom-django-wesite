from django.urls import path
from app2 import views
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('Login/',views.Login,name='Login')
]
