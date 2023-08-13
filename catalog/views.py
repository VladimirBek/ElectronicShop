from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from catalog.models import Product, Contacts, UserData


class IndexList(ListView):
    model = Product
    paginate_by = 6
    template_name = 'index.html'


class ContactCreate(CreateView):
    model = UserData
    fields = ('name', 'phone_number', 'message',)
    template_name = 'contacts.html'
    success_url = reverse_lazy('catalog:contacts')
    extra_context = {"data": Contacts.objects.get(id=1)}


class GoodsDetail(DetailView):
    model = Product
    template_name = 'goods.html'


class GoodsCreate(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'unit_price', 'produce_day')
    template_name = 'create_good.html'

    def get_success_url(self):
        return reverse_lazy('catalog:goods', args=[self.object.pk])


class GoodsUpdate(UpdateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'unit_price', 'produce_day')
    template_name = 'create_good.html'

    def get_success_url(self):
        return reverse('catalog:goods', args=[self.object.pk])


class GoodsDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')
