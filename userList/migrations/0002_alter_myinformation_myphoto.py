# Generated by Django 4.0.6 on 2022-09-01 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userList', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myinformation',
            name='myPhoto',
            field=models.URLField(default='http://drive.google.com/uc?export=view&id=', verbose_name='Мое фото'),
        ),
    ]
