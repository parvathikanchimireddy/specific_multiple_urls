from app5.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('virat/',virat,name='virat'),
    path('kavi/',kavi,name='kavi'),
]