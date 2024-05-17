from django.shortcuts import render
from django.http import HttpRequest



def inbox(request:HttpRequest):



    return render(request,'prepiske.html')
