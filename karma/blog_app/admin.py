
# Register your models here.
from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'affiche_image',
        'id',
        'titre',
        'content',
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
        'content',
        'image',
        'user',
        'date_add',
        'date_upd',
        'statut',
    )
    def affiche_image(self, obj):
        return mark_safe('<img src="{url}" width="100" height="100" > </img>'.format(url = obj.image.url))



class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'affiche_image',
        'id',
        'titre',
        'content',
        'user',
        'date_add',
        'date_upd',
        'statut',
        'views',
    )
    list_filter = (
        'user',
        'date_add',
        'date_upd',
        'statut',
        'id',
        'titre',
        'content',
        'image',
        'user',
        'date_add',
        'date_upd',
        'statut',
        'views',
    )
    def affiche_image(self, obj):
        return mark_safe('<img src="{url}" width="100" height="100" > </img>'.format(url = obj.image.url))



class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'content',
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
        'user',
        'content',
        'date_add',
        'date_upd',
        'statut',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Category, CategoryAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Comment, CommentAdmin)
