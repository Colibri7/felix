from django.db import models
from django.utils.translation import ugettext_lazy as _


class HomeModel(models.Model):
    title_1 = models.CharField(max_length=255, verbose_name=_('title_1'))
    title_2 = models.CharField(max_length=1255, verbose_name=_('title_2'))
    image = models.ImageField(upload_to='background', verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    class Meta:
        verbose_name = _('home page')
        verbose_name_plural = _('home pages')

    def __str__(self):
        return self.title_1


class ContactModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    phone = models.CharField(max_length=15, verbose_name=_('phone'))
    email = models.EmailField(verbose_name=_('email'))
    text = models.TextField(verbose_name=_('text'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
