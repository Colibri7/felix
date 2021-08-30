from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

UserModel = get_user_model()


class ProfileModel(models.Model):
    user = models.OneToOneField(UserModel, related_name='profile', on_delete=models.CASCADE, verbose_name=_('user'))
    first_name = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('first_name'))
    last_name = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('last_name'))
    phone = models.CharField(max_length=14, null=True, blank=True, verbose_name=_('phone'))
    email = models.EmailField(null=True, blank=True, verbose_name=_('email'))
    country = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('country'))
    state = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('state'))
    postcode = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('postcode'))
    address1 = models.CharField(max_length=250, null=True, blank=True, verbose_name=_('address1'))
    address2 = models.CharField(max_length=250, null=True, blank=True, verbose_name=_('address2'))
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('city'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return f'{self.first_name} {self.email}'

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')
