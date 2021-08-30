from django.db.models.signals import pre_save
from django.dispatch import receiver
from products.models import ProductsModel


@receiver(pre_save, sender=ProductsModel)
def update_price(sender, instance, *args, **kwargs):
    if instance.is_discount():
        instance.real_price = instance.price - instance.price * instance.discount / 100
    else:
        instance.real_price = instance.price