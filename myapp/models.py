import uuid

from django.db import models


def gen_unique_path(instance, filename):
    ext = filename.split('.')[-1]
    newfilename = f'{uuid.uuid4()}.{ext}'
    return f'products/{newfilename}'

CATEGORIES = [
    ('Food', 'Food category'),
    ('Drinks', 'Drinks category'),
    ('Cleaning', 'Cleaning category'),
    ('Hardware', 'Hardware category'),

]

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2) #199.85
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField(default=0)
    for_sale = models.BooleanField(default=True)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    pic = models.ImageField(upload_to=gen_unique_path, default='products/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'products'

#Run migrations
#python manage.py makemigrations
#python manage.py migrate


#python manage.py createsuperuser

#felicia 12345678