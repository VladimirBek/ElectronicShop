import django.forms
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.forms import inlineformset_factory

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Contacts, UserData, Version


class IndexList(ListView):
    model = Product
    paginate_by = 6
    template_name = 'index.html'
    ordering = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        active_versions = Version.objects.filter(status='активна')
        for product in context['object_list']:
            version = active_versions.filter(product=product)
            if version:
                product.version = {
                    'name': version[0].name,
                    'number': version[0].number,
                }

        return context


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
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy('catalog:goods', args=[self.object.pk])

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class GoodsUpdate(UpdateView):
    model = Product
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        else:
            return self.form_invalid(form)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:goods', args=[self.object.pk])


class GoodsDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')
