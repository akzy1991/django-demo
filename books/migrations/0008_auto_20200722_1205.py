# Generated by Django 2.2.14 on 2020-07-22 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_book_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='authors',
        ),
    ]
