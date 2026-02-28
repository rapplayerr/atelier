from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField('Название категории', max_length=55)
    slug = models.SlugField('url-идентификатор', max_length=255)
    description = models.TextField('Описание категории', blank = True)
    order = models.PositiveIntegerField('Порядок сортировки', default = 0)
    is_visible = models.BooleanField('Отображение', default = True)
    
    class Meta:
        verbose_name = 'Категория услуг'
        verbose_name_plural = 'Категории услуг'
        ordering = ['order','name']
    
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category_detail', kwargs = {'slug': self.slug})
class Service(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name= 'services',
        verbose_name = 'Категория' 
    )
    name = models.CharField('Название услуги', max_length=200)
    slug = models.SlugField('url-идентификатор',max_length=200)
    description = models.TextField('Описание', blank = True)
    price = models.CharField('Цена', max_length=100,blank = True)
    order = models.PositiveIntegerField('Порядок сортировки', default = 0)
    is_visible = models.BooleanField('Отображение', default = True)
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['category','order','name']
        unique_together = ['category','slug']
    def __str__(self):
        return f'{self.category.name} - {self.name}'
    def get_absolute_url(self):
        return reverse("service_detail", args=[self.category.slug, self.slug])
    

    
    
    
