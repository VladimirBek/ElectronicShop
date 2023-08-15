from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify

from blog.models import Blog


class IndexList(ListView):
    model = Blog
    paginate_by = 6

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(published=True)
        return qs


class BlogDetail(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogCreate(CreateView):
    model = Blog
    fields = ('title', 'body', 'preview', 'published',)

    def get_success_url(self):
        return reverse_lazy('blog:articles', args=[self.object.slug])

    def form_valid(self, form):
        if form.is_valid():
            new_form = form.save()
            new_form.slug = slugify(new_form.title) + str(new_form.pk)
            new_form.save()
        return super().form_valid(form)


class BlogUpdate(UpdateView):
    model = Blog
    fields = ('title', 'body', 'preview', 'published',)

    def get_success_url(self):
        return reverse_lazy('blog:articles', args=[self.object.slug])

    def form_valid(self, form):
        if form.is_valid():
            new_form = form.save()
            new_form.slug = slugify(new_form.title) + str(new_form.pk)
            new_form.save()
        return super().form_valid(form)


class BlogDelete(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:index')
