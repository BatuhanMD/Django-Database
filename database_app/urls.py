from django.urls import path
from . import views

app_name = "database_app"
urlpatterns = [
    path('',views.index, name="index"),
    
]