# Generated by Django 3.2.6 on 2021-08-03 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='data_nascimento',
            field=models.IntegerField(),
        ),
    ]