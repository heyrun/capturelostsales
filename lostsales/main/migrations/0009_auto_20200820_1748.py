# Generated by Django 3.1 on 2020-08-20 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200820_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='Description',
            new_name='description',
        ),
    ]
