# Generated by Django 4.0.6 on 2022-08-03 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_book_image_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]