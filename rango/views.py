from django.shortcuts import render

# Andrew Partridge
# 18/01/2019

from django.http import HttpResponse

## sends a message to the client
def index(request):
    return HttpResponse("Rango says hey there partner!")
