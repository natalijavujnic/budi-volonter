from django.shortcuts import render,HttpResponse
from . import models
from . import models
def welcome(request):
   return render(request,'main_page.html') 
