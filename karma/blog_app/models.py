from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    titre = models.CharField(max_length=255,)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_category')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_blog_category')
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'





class Article(models.Model):
    titre = models.CharField(max_length=255,)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_article')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_article')
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)
    categories = models.ManyToManyField("category", related_name='categories')
    views = models.IntegerField()

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_blog_comment')
    content = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.user.name

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'