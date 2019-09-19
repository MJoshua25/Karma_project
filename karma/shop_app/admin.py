

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


class CategoryAdmin(admin.ModelAdmin):
    def affiche_image(self, obj):
        return mark_safe('<img src="{url}" width="100" height="100" > </img>'.format(url = obj.image.url))

    list_display = (
        'affiche_image',
        'id',
        'titre',
        'description',
        'user',
        'date_add',
        'date_upd',
        'statut',
    )
    list_filter = (
        'user',
        'date_add',
        'date_upd',
        'statut',
        'id',
        'titre',
        'description',
        'user',
    )




class ProductAdmin(admin.ModelAdmin):
    def affiche_image(self, obj):
        return mark_safe('<img src="{url}" width="100" height="100" > </img>'.format(url = obj.image.url))


    list_display = (
        'affiche_image',
        'id',
        'name',
        'price',
        'availibility',
        'stock',
        'category',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'availibility',
        'category',
        'date_add',
        'date_upd',
        'id',
        'name',
        'price',
    )
    search_fields = ('name',)
   
class CommentAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'content', 'date_add', 'product', 'statut')
    list_filter = (
        'user',
        'date_add',
        'product',
        'statut',
        'id',
        'user',
        'content',
        'date_add',
        'product',
        'statut',
    )


class RateAdmin(admin.ModelAdmin):

    list_display = ('id', 'rate', 'user', 'product', 'date_add', 'date_upd')
    list_filter = (
        'user',
        'product',
        'date_add',
        'date_upd',
        'id',
        'rate',
        'user',
        'product',
        'date_add',
        'date_upd',
    )


class PanierAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'date_add', 'date_upd')
    list_filter = (
        'user',
        'date_add',
        'date_upd',
        'id',
        'user',
        'date_add',
        'date_upd',
    )
    raw_id_fields = ('items',)


class ItemsAdmin(admin.ModelAdmin):

    list_display = ('id', 'product', 'quantite', 'date_add', 'date_upd','prix_unitaire','prix_total')
    list_filter = (
        'product',
        'date_add',
        'date_upd',
        'id',
        'product',
        'quantite',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Category, CategoryAdmin)
_register(models.Product, ProductAdmin)
_register(models.Comment, CommentAdmin)
_register(models.Rate, RateAdmin)
_register(models.Panier, PanierAdmin)
_register(models.Items, ItemsAdmin)
