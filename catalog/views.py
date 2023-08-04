from django.shortcuts import render
from django.views.generic.detail import DetailView

from catalog.models import Product, Contacts


def index(request):
    products = Product.objects.all().values('name').order_by('-pk')
    for product in products[:5]:
        print(f'{product["name"]}')
    return render(request, 'index.html')


def contacts(request):
    data = Contacts.objects.get(id=1)
    return render(request, 'contacts.html', context={'data': data})
