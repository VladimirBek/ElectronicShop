from django.urls import path

from catalog.views import index, contacts, goods

app_name = 'catalog'

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('<int:pk>/goods/', goods, name='goods'),
]
