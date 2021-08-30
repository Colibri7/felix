from django import template
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.templatetags.static import static

from products.models import ProductsModel

register = template.Library()


@register.simple_tag
def get_lang_url(request, lang):
    url = request.path.split('/')
    url[1] = lang

    return '/'.join(url)


@register.simple_tag
def get_price(request, x):
    price = request.GET.get('price')
    if price:
        return price.split(';')[x]
    return 'null'


@register.simple_tag
def get_wishlist_icon(request, pk):
    product = get_object_or_404(ProductsModel, pk=pk)
    if request.user in product.wishlist.all():
        return static('/img/icon/heartr.png')
    else:
        return static('/img/icon/heart.png')


@register.filter
def in_cart(product, request):
    return product.pk in request.session.get('cart', [])


@register.simple_tag
def cart_count(request):
    return len(request.session.get('cart', []))


@register.simple_tag
def cart_sum(request):
    cart = request.session.get('cart')
    if not cart:
        return 0
    return ProductsModel.get_from_cart(request). \
        aggregate(Sum('real_price')).get('real_price__sum', 0)
