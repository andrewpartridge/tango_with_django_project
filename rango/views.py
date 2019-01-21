from django.shortcuts import render

# Andrew Partridge
# Last edited: 20/01/2019

from django.http import HttpResponse


def index(request):
    # Construct a dict. to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    # Return a rendered response to send to the client
    # Make use of the shortcut function for ease of use
    # Note that the first parameter is the template we wish to use
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'italicmessage': "This is Dean Castle, unrelated to Rango"}
    
    return render(request, 'rango/about.html', context=context_dict)
