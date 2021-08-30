# Generated by Django 3.2.4 on 2021-07-17 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created_at'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='address1',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='address1'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='address2',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='address2'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='last_name'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='phone',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='postcode',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='postcode'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='state'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]