from django.urls import path

from catalog.views import IndexList, ContactCreate, GoodsCreate, GoodsDetail, GoodsUpdate, GoodsDelete

app_name = 'catalog'

urlpatterns = [
    path('', IndexList.as_view(), name='index'),
    path('contacts/', ContactCreate.as_view(), name='contacts'),
    path('goods/<int:pk>/', GoodsDetail.as_view(), name='goods'),
    path('create_good/', GoodsCreate.as_view(), name='create_good'),
    path('update_good/<int:pk>/', GoodsUpdate.as_view(), name='update_good'),
    path('delete_good/<int:pk>/', GoodsDelete.as_view(), name='delete_good'),

]
