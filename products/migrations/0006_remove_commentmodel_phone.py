# Generated by Django 3.2.4 on 2021-07-01 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_commentmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentmodel',
            name='phone',
        ),
    ]