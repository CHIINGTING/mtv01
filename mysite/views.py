from django.http import HttpResponse
from django.shortcuts import render
from mysite.models import Product


# Create your views here.
def about(request):
    html = '''<!DOCTYPE html>
    <html>
        <head>
            <title>About Myself</title>
        </head>
        <body>
            <h2>Andy Wood</h2>
            <hr>
            <p>Hi, I am Andy Wood. Nice to meet you!</p>
        </body>
    </html>
    '''
    return HttpResponse(html)


def listing(request):
    html = '''<!DOCTYPE html>
    <html>
        <head>
            <meta charset='utf-8'>
            <title>中古機列表</title>
        </head>
        <body>
            <h2>以下是目前本店販售中的產品列表</h2>
            <hr>
            <table width=400 border=1 bgcolor='#ccffcc'>
                {}
            </table>
        </body>
        <body>
            <h2>以下是目前本店販售中的缺貨列表</h2>
            <hr>
            <table width=400 border=1 bgcolor='#ccffcc'>
                {}
            </table>
        </body>
    </html>
    '''
    products = Product.objects.all().order_by('price').exclude(qty=0)
    tags = '<tr><td>品名</td><td>售價</td><td>庫存量</td></tr>'
    for p in products:
        tags = tags + '<tr><td>{}</td>'.format(p.name)
        tags = tags + '<td>{}</td>'.format(p.price)
        tags = tags + '<td>{}</td></tr>'.format(p.qty)

    outStock = Product.objects.all().order_by('price').filter(qty=0)
    tags2 = '<tr><td>品名</td><td>售價</td><td>庫存量</td></tr>'
    for p in outStock:
        tags2 = tags2 + '<tr><td>{}</td>'.format(p.name)
        tags2 = tags2 + '<td>{}</td>'.format(p.price)
        tags2 = tags2 + '<td>{}</td></tr>'.format(p.qty)

    return HttpResponse(html.format(tags, tags2))
