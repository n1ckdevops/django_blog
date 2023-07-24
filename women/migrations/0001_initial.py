# Generated by Django 4.2 on 2023-05-23 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Category')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Women',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='Article text')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Photo')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Creation time')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Published time')),
                ('is_published', models.BooleanField(default=True, verbose_name='Published')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='women.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Woman of the World',
                'verbose_name_plural': 'Women of the World',
                'ordering': ['time_create', 'title'],
            },
        ),
    ]
