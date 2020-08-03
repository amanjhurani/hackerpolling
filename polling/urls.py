
from django.urls import path, include
from .views import *
urlpatterns = [
    path('',index, name='index'),
    path('hackerlist',hacker_list, name='hackerlist'),
    path('hackerdetail',user_detail, name='userdetail'),
    path('voted',vote, name='vote')

]
