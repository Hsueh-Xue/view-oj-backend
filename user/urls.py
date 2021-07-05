from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'add$', views.AddUserView.as_view()),
    url(r'ranklist$', views.GetRatingView.as_view()),
]
