from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    #greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


def madd(request):
	return render(request,"madd.html")


def add(request):
	return render(request,"mymath.html", {"myop":"add"})

def sum(request):
	return render(request,"mymath.html", {"myop":"sum"})

def divide(request):
	return render(request,"mymath.html", {"myop":"divide"})

def result(request):
	val1 = int(request.GET['num1'])
	val2 = int(request.GET['num2'])
	myres = val1 + val2
	return render(request, 'result.html', {'results':myres})

def multiplay(request):
	return render(request,"mymath.html", {"myop":"multiplay"})