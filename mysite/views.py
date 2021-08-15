import random
from django.shortcuts import render
from mysite.models import Product


# Create your views here.
def about(request):
    quotes = ['Everything before the word ‘but’ is horseshit.',
              'Some wounds never truly heal, and bleed again at the slightest word.',
              'The man who passes the sentence should swing the sword.']
    quote = random.choice(quotes)
    return render(request, 'about.html', locals())


def listing(request):
    products = Product.objects.all().order_by('price').exclude(qty=0)
    outStock = Product.objects.all().order_by('price').filter(qty=0)
    return render(request, 'list.html', locals())