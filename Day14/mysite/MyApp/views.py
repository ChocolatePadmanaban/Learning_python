from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import HttpResponse
# import datetime 
from datetime import datetime, timezone

def say_hello(request, name):
    return HttpResponse("Hello " +name)


def current_datetime(request):
    now = datetime.now()
    return render_to_response("current_datetime.html",
    {'current_date': now})

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now()+ datetime.timedelta(hours = offset)
    html = """<html><body>In %s hours(s), it will be %s</body></html>
    """%(offset,dt)
    return HttpResponse(html)