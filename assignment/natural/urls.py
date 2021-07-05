from django.urls import path

from . import views

urlpatterns=[
		path('',views.home,name='home'),
		path('factor',views.factor,name='factor')
]