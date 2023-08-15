from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from pytils.translit import slugify

from blog.models import Blog
from config import settings


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
        if self.object.view_count == 100:
            obj_title = self.object.title
            send_mail(
                f'Congrats, {obj_title} owner, we have some news for you!',
                f"Your article {obj_title} got first 100 views!",
                settings.EMAIL_HOST_USER,
                recipient_list=[self.object.email_address])
        return self.object


class BlogCreate(CreateView):
    model = Blog
    fields = ('title', 'body', 'preview', 'published', 'email_address')

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
    fields = ('title', 'body', 'preview', 'published', 'email_address')

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
