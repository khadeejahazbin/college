from django.db import models
from django.urls import reverse


# Create your models here.
class Department(models.Model):
    objects = None
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
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
