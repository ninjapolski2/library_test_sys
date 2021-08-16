# Generated by Django 3.2.6 on 2021-08-14 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=2000)),
                ('identificator', models.CharField(max_length=12)),
                ('available', models.BooleanField(default=True, verbose_name='dostępność')),
            ],
        ),
        migrations.CreateModel(
            name='PlaceOfTheBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_the_room', models.IntegerField(max_length=3)),
                ('shelf_identificator', models.CharField(max_length=15)),
                ('identificator_of_the_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
            ],
        ),
    ]
