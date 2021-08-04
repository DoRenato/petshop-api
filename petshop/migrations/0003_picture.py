# Generated by Django 3.2.6 on 2021-08-03 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petshop', '0002_alter_pet_data_nascimento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='')),
                ('petId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petshop.pet')),
            ],
        ),
    ]