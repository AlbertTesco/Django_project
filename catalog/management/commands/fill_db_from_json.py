import json

from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    """
    Пока эта команда заполняет БД моделью Category!!!
    """

    help = 'Загрузить данные из JSON-файла в базу данных и очистить базу данных'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file with data to load')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']

        try:
            with open(json_file, 'r') as file:
                data = json.load(file)

            Category.objects.all().delete()
            Product.objects.all().delete()

            for item in data:
                model = item["model"]
                pk = item["pk"]
                fields = item["fields"]

                if model == 'catalog.category':
                    category = Category.objects.create(
                        id=pk,
                        name=fields['name'],
                        description=fields['description']
                    )
                    category.save()

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('File not found.'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Invalid JSON format.'))
