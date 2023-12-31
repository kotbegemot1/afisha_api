# Generated by Django 4.2.5 on 2023-10-04 10:52

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
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=100, verbose_name='Псавдоним')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('image', models.ImageField(upload_to='artists/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Артисты и организаторы',
                'verbose_name_plural': 'Артисты и организаторы',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Место')),
                ('descrtption', models.TextField(verbose_name='Описание')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Адрес проведения',
                'verbose_name_plural': 'Адрес проведения',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('descrtption', models.TextField(verbose_name='Описание')),
                ('poster', models.ImageField(upload_to='events/', verbose_name='Постер')),
                ('event_date', models.DateTimeField(verbose_name='Время проведения')),
                ('is_past', models.BooleanField(default=False, verbose_name='Прошедшее событие')),
                ('is_draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('artists', models.ManyToManyField(related_name='event_artist', to='afisha_api.artist', verbose_name='Участники')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_category', to='afisha_api.category')),
                ('favourite', models.ManyToManyField(blank=True, related_name='event_favourite', to=settings.AUTH_USER_MODEL, verbose_name='Избранное')),
                ('organizer', models.ManyToManyField(related_name='event_organizer', to='afisha_api.artist', verbose_name='Организаторы')),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_place', to='afisha_api.place')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afisha_api.event', verbose_name='Событие')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='afisha_api.comments', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
