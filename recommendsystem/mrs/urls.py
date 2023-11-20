from django.urls import path
from .import views
from data import autocomplete

urlpatterns=[
    path('',views.home,name='home'),
    path('autocomplete/', autocomplete.autocompletelist, name='autocomplete'),
    path('recommend',views.recommend,name='recommend')
]