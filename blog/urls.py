from django.urls import path
from .apps import BlogConfig
from .views import IndexList, BlogDetail, BlogCreate, BlogUpdate, BlogDelete

app_name = BlogConfig.name

urlpatterns = [
    path('blog/', IndexList.as_view(), name='index'),
    path('blog/<slug:slug>/', BlogDetail.as_view(), name='articles'),
    path('create_article/', BlogCreate.as_view(), name='create_article'),
    path('update_article/<slug:slug>/', BlogUpdate.as_view(), name='update_article'),
    path('delete_article/<slug:slug>/', BlogDelete.as_view(), name='delete_article'),

]
