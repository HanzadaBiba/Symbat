from django.db import models
from django.urls import reverse
# Create your models here.
from django.contrib.auth.models import User
class Method(models.Model):
    image=models.ImageField(upload_to='image/')
    name=models.CharField(max_length=255)
    slug=models.SlugField()
    description=models.TextField()
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home:method_detail',args=[self.slug])
    class Meta:
        verbose_name_plural='Кызмет'
        verbose_name='Кызмет'

class Order(models.Model):
    full_name=models.CharField(max_length=255,verbose_name='ТАӘ')
    oblis=models.CharField(max_length=255,verbose_name='Облыс')
    city=models.CharField(max_length=255,verbose_name='Кала')
    description=models.TextField(verbose_name='Өтініш мақсаты')
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    method=models.ForeignKey(Method,on_delete=models.CASCADE)
    def __str__(self):
        return  self.full_name
    class Meta:
        verbose_name_plural='Өтініш'
        verbose_name='Өтініш'
