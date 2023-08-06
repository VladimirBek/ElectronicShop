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
