# Generated by Django 4.0.6 on 2022-07-13 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]