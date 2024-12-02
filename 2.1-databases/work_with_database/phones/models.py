from django.db import models
from django.template.defaultfilters import slugify

class Phone(models.Model):
    name = models.CharField(max_length=80)
    image = models.URLField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    lte_exists = models.BooleanField(null=False)
    slug = models.SlugField(max_length = 80, unique=True)
    
    def __str__(self):
        return f'{self.name}; {self.price}; {self.image}; {self.release_date}; {self.lte_exists}; {self.slug}'
    
    def save(self,  *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Phone, self).save(*args, **kwargs)