# Generated by Django 3.2.5 on 2021-08-16 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_placeofthebook_number_of_the_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shelf_identificator', models.CharField(max_length=15, verbose_name='pokój|dział/półka')),
                ('filia', models.IntegerField(max_length=2, verbose_name='filia')),
                ('address', models.TextField(max_length=1000, verbose_name='adres')),
                ('availability', models.BooleanField(default=True, verbose_name='dostępność')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='available',
        ),
        migrations.DeleteModel(
            name='PlaceOfTheBook',
        ),
        migrations.AddField(
            model_name='place',
            name='identificator_of_the_book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book'),
        ),
    ]