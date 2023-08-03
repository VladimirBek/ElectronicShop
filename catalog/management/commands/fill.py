import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('catalog/management/commands/catalog_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        for data_fill in data:
            product = data_fill['fields']
            if product['category'] == 1:
                product['category'] = Category.objects.get(id=1)
            elif product['category'] == 2:
                product['category'] = Category.objects.get(id=2)
            elif product['category'] == 3:
                product['category'] = Category.objects.get(id=3)
            elif product['category'] == 4:
                product['category'] = Category.objects.get(id=4)
            Product.objects.create(**product)
