# Generated by Django 4.0.6 on 2022-07-12 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('pages', models.CharField(max_length=200)),
                ('published_at', models.DateField(auto_now_add=True)),
                ('is_available', models.BooleanField(default=False)),
            ],
        ),
    ]