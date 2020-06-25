from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    field_name = models.ManyToManyField('FieldScope',
                                        through='ArticleField',
                                        through_fields=('article', 'field'),
                                        related_name='fields_names',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class FieldScope(models.Model):
    name = models.CharField(max_length=40, verbose_name='Раздел')

    class Meta:
        verbose_name = 'Тематика'
        verbose_name_plural = 'Тематики'

    def __str__(self):
        return self.name


class ArticleField(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья')
    field = models.ForeignKey(FieldScope, on_delete=models.CASCADE, verbose_name='Раздел', related_name='field')
    is_main_bool = models.BooleanField(verbose_name='Основной')

    def __str__(self):
        return self.field
