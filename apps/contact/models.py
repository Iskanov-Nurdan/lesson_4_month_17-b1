from django.db import models


# Create your models here.
class Translate(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок баннера")
    hotline = models.CharField(max_length=255, verbose_name="Горячая линия")
    our_location = models.CharField(max_length=255, verbose_name="Локация")
    email = models.CharField(max_length=255, verbose_name="Официальная почта")

    def __str__(self) -> str:
        return f"{self.title} - {self.hotline}"

    class Meta:
        verbose_name = ""
        verbose_name_plural = "Перевод страницы контакты"
