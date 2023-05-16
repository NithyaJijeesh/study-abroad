from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils.text import capfirst
from .models import *
import random

def index(request):
   
    return render(request,'index.html')


