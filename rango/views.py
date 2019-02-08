from django.shortcuts import render

# Andrew Partridge
# Last edited: 20/01/2019

from django.http import HttpResponse

from rango.models import Category
from rango.models import Page

def index(request):
    # Construct a dict. to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    
    context_dict = {'categories': category_list, 'pages': page_list}

    # Return a rendered response to send to the client
    # Make use of the shortcut function for ease of use
    # Note that the first parameter is the template we wish to use
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'italicmessage': "This is Dean Castle, unrelated to Rango"}
    
    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages

        context_dict['categpry'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)
