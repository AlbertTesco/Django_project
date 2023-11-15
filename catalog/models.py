from django.db import models

from config import settings

NULLABLE = {
    'blank': True,
    'null': True,
}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name="Картинка")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    purchase_price = models.FloatField(verbose_name="Цена")
    created_date = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    last_modified_date = models.DateField(auto_now=True, verbose_name="Дата последнего изменения")
    is_published = models.BooleanField(default=False, verbose_name="Признак опубликованности")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Продавец')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

        permissions = [
            (
                'set_is_published',
                'Can is_published'
            ),
            (
                'set_description',
                'Can description'
            ),
            (
                'set_category',
                'Can category'
            )

        ]

    @property
    def active_version(self):
        return Version.objects.filter(is_active=True, product=self).first()

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    version_num = models.FloatField(verbose_name="Номер версии")
    version_name = models.CharField(max_length=100, verbose_name="Название версии")
    is_active = models.BooleanField(default=False, verbose_name='Признак активности')

    def __str__(self):
        return f'{self.version_num}-{self.version_name}'

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Эл. почта")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    address = models.TextField(verbose_name="Адрес")

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.name
