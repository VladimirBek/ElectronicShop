from django.db import models
from django.utils.timezone import now

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок')
    slug = models.CharField(max_length=200, unique=True, verbose_name='URL')
    body = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(verbose_name='изображение (превью)', **NULLABLE)
    create_date = models.DateField(verbose_name='дата создания', default=now)
    published = models.BooleanField(verbose_name='признак публикации', default=False)
    view_count = models.IntegerField(verbose_name='колличество просмотров', default=0)

    def __str__(self):
        return f'{self.title}, просмотры: {self.view_count}'

    class Meta:
        verbose_name = 'блоговая запись'
        verbose_name_plural = 'блоговые записи'
