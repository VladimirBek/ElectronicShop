import datetime

from django.shortcuts import render

from catalog.models import Product, Contacts, UserData, Category


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
    context = {'objects_list': Category.objects.all()}
    if request.method == 'POST':
        if request.POST.get('category') == 'Компьютеры':
            category = Category.objects.get(id=1)
        elif request.POST.get('category') == 'Мониторы':
            category = Category.objects.get(id=2)
        elif request.POST.get('category') == 'Телефоны':
            category = Category.objects.get(id=3)
        elif request.POST.get('category') == 'Смартфоны':
            category = Category.objects.get(id=4)
        name = request.POST.get('name')
        description = request.POST.get('description')
        unit_price = request.POST.get('unit_price')
        produce_day = request.POST.get('produce_day')
        last_change = datetime.date.today()
        Product.objects.create(name=name, description=description, category=category, unit_price=unit_price,
                               produce_day=produce_day, last_change=last_change)
    return render(request, 'create_good.html', context)
