# Generated by Django 4.2.7 on 2023-12-21 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photofornews',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
