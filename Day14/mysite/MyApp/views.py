from django.shortcuts import render, render_to_response
from MyApp.models import Publisher
from MyApp.models import Book
from django.forms import ModelForm
# Create your views here.
from django.http import HttpResponse
# import datetime 
from datetime import datetime, timezone

class ArticleForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors','publisher','publication_date']


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

def search_form(request):
    return render_to_response("search_from.html")

def search(request):
    if 'q'in request.GET:
        message = request.GET['q']
        checkin = Publisher.objects.filter(name__contains=message)
        if checkin:
            message = checkin.values()
        else:
            message = "not in DB"
    else:
        message = 'You submitted an empty form'
    return HttpResponse(message)

def GetForm(request):
    articleForm = ArticleForm()
    return HttpResponse(articleForm)

def getColor(request):
    return render_to_response("myCookie.html")

def setColor(request):
    if 'fav_color' in request.GET:
        response = HttpResponse("Your Favorite Color is now %s" % request.GET["fav_color"])
        response.set_cookie("fav_color",request.GET['fav_color'])
        return response
    else:
        return HttpResponse("You didnot give a favorite color")

def show_color(request):
    if 'fav_color' in request.COOKIES:
        return HttpResponse("Your favorite color is %s" % request.COOKIES['favorite_color'])
    else:
        return HttpResponse("You donot have a favorite color in cookie")

def login(request):
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            return HttpResponse("You are logged in")