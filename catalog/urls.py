from django.urls import path

from catalog.views import index, contacts, goods, create_good

app_name = 'catalog'

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('<int:pk>/goods/', goods, name='goods'),
    path('create_good/', create_good, name='create_good'),
]
