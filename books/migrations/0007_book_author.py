# Generated by Django 2.2.14 on 2020-07-22 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20200722_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='books.Author'),
        ),
    ]
