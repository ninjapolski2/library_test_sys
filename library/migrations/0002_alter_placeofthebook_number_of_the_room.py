# Generated by Django 3.2.6 on 2021-08-14 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeofthebook',
            name='number_of_the_room',
            field=models.IntegerField(),
        ),
    ]
