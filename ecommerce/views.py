from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''

    return HttpResponse('Welcome to 6410742560 ชญานิษฐ์ โลหะกิจจา views!')

def item_view(request, item_id):

    context_data = {
        "item_id": item_id
    }

    return render(request, 'index.html', context = context_data)

def home_view(request):
    return HttpResponse('Home Page')

def category_view(request):
    return HttpResponse('Category Page')

def product_view(request):
    return HttpResponse('Product Page')

def checkout_view(request):
    return HttpResponse('Checkout Page')

def contact_view(request):
    return HttpResponse('Contact Page')