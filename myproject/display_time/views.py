from email.utils import localtime
from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

# Create your views here.
def index(request):
    context = {
        "time": datetime.now()
    }
    
    return render(request,'display_time.html', context)
    

def time_display(reques):
    return redirect('/')

