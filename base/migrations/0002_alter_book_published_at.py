# Generated by Django 4.0.6 on 2022-07-12 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_at',
            field=models.DateField(auto_now=True),
        ),
    ]
