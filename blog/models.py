from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(
        verbose_name="Превью (изображение)", blank=True, null=True
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания", null=True, blank=True
    )
    is_published = models.BooleanField(verbose_name="Признак публикации", default=False)
    counter_view = models.IntegerField(verbose_name="Количество просмотров", default=0)

    class Meta:
        verbose_name = "Блоговая запись"
        verbose_name_plural = "Блоговые записи"

    def __str__(self):
        return self.title
