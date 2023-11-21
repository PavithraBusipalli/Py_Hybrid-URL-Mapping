from django.urls import path
from generic.views import * 

app_name='gen'

urlpatterns=[
    path('generic2/',generic2,name='generic2'),
]