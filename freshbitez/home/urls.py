from django.urls import path
from . import views
from .feed import newproducts

urlpatterns = [
    path("",views.index,name="homepage"),
    path("login/",views.login,name="loginpage"),
    path("register/",views.register,name="registerpage"),
    path("logout/",views.logout),
    path('feed/',newproducts()),

]
