from catalog.models import Category
from django.conf import settings
from django.core.cache import cache


def get_category_set():
    if settings.CACHE_ENABLED:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)

        return category_list
