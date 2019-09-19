# Generated by Django 2.2.3 on 2019-09-19 00:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('statut', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_blog_comment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='blog_category')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('statut', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_blog_category', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='blog_article')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('statut', models.BooleanField(default=True)),
                ('views', models.IntegerField()),
                ('categories', models.ManyToManyField(related_name='categories', to='blog_app.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_article', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]
