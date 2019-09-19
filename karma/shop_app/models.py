from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    titre = models.CharField(max_length=255,)
    description = models.TextField()
    image = models.ImageField(upload_to='shop_category')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_category')
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)
    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField(max_length=255,)
    price = models.CharField(max_length=255,)
    availibility = models.BooleanField(default=True)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='category_product')
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    content = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product_comments')
    statut = models.BooleanField(default=True)
    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

class Rate(models.Model):
    rate = models.IntegerField(choices=[
        (1, 'mauvais'),
        (2, 'naze'),
        (3, 'abordable'),
        (4, 'super'),
        (5,'excelent')
    ])
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_rate')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product_rate')
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.rate

    class Meta:
        verbose_name = 'Rate'
        verbose_name_plural = 'Rates'

class Panier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_panier')
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    items = models.ManyToManyField('Items')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Panier'
        verbose_name_plural = 'Paniers'

class Items(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product_items')
    quantite = models.IntegerField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    @property
    def prix_unitaire(self):
        return self.product.price
    @property
    def prix_total(self):
        return int(self.prix_unitaire)*int(self.quantite)
    def __str__(self):
        return self.product.name
    class Meta:
        verbose_name = 'Items'
        verbose_name_plural = 'Items'