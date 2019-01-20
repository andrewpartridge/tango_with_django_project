from django.shortcuts import render

# Andrew Partridge
# Last edited: 20/01/2019

from django.http import HttpResponse

## sends a message to the client
def index(request):
    return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("Rango says here is the about page. <br/> <a href='/rango'/>Index</a>")
