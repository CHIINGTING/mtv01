import random
from django.shortcuts import render
from mysite.models import Product
from django.http import Http404


# Create your views here.
def site(request):
    quotes = ['Everything before the word ‘but’ is horseshit.',
              'Some wounds never truly heal, and bleed again at the slightest word.',
              'The man who passes the sentence should swing the sword.']
    quote = random.choice(quotes)
    return render(request, 'main.html', locals())


def about(request):
    name = 'the site of Deep'
    return render(request, 'about.html', locals())


def listing(request):
    products = Product.objects.all().order_by('price').exclude(qty=0)
    outStock = Product.objects.all().order_by('price').filter(qty=0)
    return render(request, 'list.html', locals())


def disDetail(request, sku):
    try:
        p = Product.objects.get(sku=sku)
    except p.DoesNotExist:
        raise Http404('找不到品項編號')
    return render(request, 'dis.html', locals())
