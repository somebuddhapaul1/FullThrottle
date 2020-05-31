from django.urls import path
from . import views

app_name = 'populate_data'

urlpatterns = [
    path('show_json', views.show_json, name='index'),
]
