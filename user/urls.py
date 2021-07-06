from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'add$', views.AddUserView.as_view()),
    url(r'ranklist$', views.GetRatingView.as_view()),
    url(r'auth$', views.AuthView.as_view()),
    url(r'modifyNickname$', views.ModifyNicknameView.as_view()),
    url(r'modifyPassword$', views.ModifyPasswordView.as_view()),
    url(r'modifyCodeforces$', views.ModifyCodeforcesView.as_view()),
]
