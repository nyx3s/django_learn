from django.shortcuts import render
import datetime as date
# Create your views here.

def index(request):
    now = date.datetime.now()
    return render(request, "newyear/index.html",{"now":now.day == 1 and now.month == 1
})
