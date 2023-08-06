from django.shortcuts import render

from catalog.models import Product, Contacts, UserData


def index(request):
    context = {'objects_list': Product.objects.all()}
    return render(request, 'index.html', context)


def contacts(request):
    data = Contacts.objects.get(id=1)
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        massage = request.POST.get('message')
        UserData.objects.create(name=name, phone_number=phone, message=massage)
    return render(request, 'contacts.html', context={'data': data})


def goods(request, pk):
    context = {'object': Product.objects.get(pk=pk)}
    return render(request, 'goods.html', context)


def create_good(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = request.POST.get('category')
        unit_price = request.POST.get('unit_price')
        produce_day = request.POST.get('produce_day')
        last_change = request.POST.get('produce_day')
        UserData.objects.create(name=name, phone_number=phone, message=massage)