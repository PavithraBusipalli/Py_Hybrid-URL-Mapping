from django.urls import path
from specific.views import *

app_name='spe'

urlpatterns=[
    path('specific2/',specific2,name='specific2'),
]