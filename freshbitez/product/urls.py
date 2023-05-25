from django.urls import path
from . import views

urlpatterns = [
    path("",views.product,name="productspage"),
    path("details/",views.details,name="detailspage"),
    path("cmt/",views.commentsub,name="commentbox")

]