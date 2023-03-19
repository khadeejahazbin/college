from django.db import models
from django.urls import reverse


# Create your models here.
class Department(models.Model):
    objects = None
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='department', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'department'
        verbose_name_plural = 'departments'

    def get_url(self):
        return reverse('schools:allDepart', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Order(models.Model):
    objects = None
    first_name=models.CharField(max_length=50)
    DOB=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    phone_no=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=250)
    department=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    purpose=models.CharField(max_length=50)
    material_provide=models.CharField(max_length=50)

    class Meta:
        ordering = ('first_name',)
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self):
        return '{}'.format(self.first_name)