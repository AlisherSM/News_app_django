from django.db import models

class News(models.Model):
    title = models.CharField("Заголовок", max_length=35)
    text = models.TextField("Текст")
    image = models.ImageField("Картинка")
    published_date = models.DateTimeField("Дата публикации",auto_now_add=True)
    is_published = models.BooleanField("Опубликовано",default=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

