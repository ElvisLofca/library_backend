# Generated by Django 4.0.6 on 2022-07-14 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_book_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
