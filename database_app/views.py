from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    fighter_data = models.Fighter.objects.all()
    fighter_context = {"fighter": fighter_data}
    return render(request,'database_app/index.html',context=fighter_context)