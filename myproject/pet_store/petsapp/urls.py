from django.urls import path,include
from . import views
urlpatterns=[
    path('list_pets',views.list_pets,name="list_pets"),
    path('<int:id>',views.pet_detail,name='petdetail'),
    path('',views.register),
    path('signup',views.signup),
    path('login',views.user_login),
    path('profile',views.profile),
    path('logout',views.user_logout)]
