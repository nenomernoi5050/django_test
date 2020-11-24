from django.db import models
from news.utils import transliterate


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название населенного пункта",
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, verbose_name="URL", unique=True)

    class Meta:
        verbose_name="Название населенного пункта"
        verbose_name_plural="Название населенных пунктов"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = transliterate(self.name)
        super().save(*args,*kwargs)


class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name="Язык програмирования",
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, verbose_name="URL",unique=True)

    class Meta:
        verbose_name="Название языка программирования"
        verbose_name_plural="Название языков программирования"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = transliterate(self.name)
        super().save(*args,*kwargs)


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Заголовок вакансии')
    company = models.CharField(max_length=250, verbose_name='Компания')
    description = models.TextField(verbose_name='Описание вакансии')
    city = models.ForeignKey('City', on_delete=models.CASCADE,
                             verbose_name='Город')
    language = models.ForeignKey('Language', on_delete=models.CASCADE,
                                 verbose_name='Язык программирования')
    timestamp = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name='Название вакансии'
        verbose_name_plural='Вакансии'
    
    def __str__(self):
        return self.title