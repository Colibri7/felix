# Generated by Django 3.2.4 on 2021-07-13 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_commentmodel_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=550)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'gender',
                'verbose_name_plural': 'genders',
            },
        ),
    ]