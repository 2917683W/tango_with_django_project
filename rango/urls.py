from django.urls import path
from rango import views

urlpatterns = [
  path('',views.indexm, name='index')
]
