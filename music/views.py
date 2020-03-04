# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from .models import Album

# Create your views here.

def index(request):
    my_dict={
        'A':"Melvin is in thrissur",
        'data':""
            } 
    return render(request,'form.html',context=my_dict)

def postData(request):
    a=request.POST.get('username')
    my_dict={
        'A':a,
        'data':""
            } 
    if request.method=="POST":
        AlData=Album()
        AlData.artist =request.POST.get('username')
        AlData.album_title ="Jazz Solutions"
        AlData.genre ="My Song"
        AlData.album_logo ="Data"
        AlData.save()

    return HttpResponse(a)


def loadData(request):
    AlData=Album.objects.all()
    my_dict={
        'data':AlData
        }  

    return render(request,'table.html',context=my_dict)