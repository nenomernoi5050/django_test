# Generated by Django 3.1.3 on 2020-11-25 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название населенного пункта')),
                ('slug', models.CharField(blank=True, max_length=50, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Название населенного пункта',
                'verbose_name_plural': 'Название населенных пунктов',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Язык програмирования')),
                ('slug', models.CharField(blank=True, max_length=50, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Название языка программирования',
                'verbose_name_plural': 'Название языков программирования',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок вакансии')),
                ('company', models.CharField(max_length=250, verbose_name='Компания')),
                ('description', models.TextField(verbose_name='Описание вакансии')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_test_project.city', verbose_name='Город')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_test_project.language', verbose_name='Язык программирования')),
            ],
            options={
                'verbose_name': 'Название вакансии',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]
