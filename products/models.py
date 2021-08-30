from datetime import datetime
from django.utils.translation import ugettext_lazy as _
import pytz
from django.contrib.auth import get_user_model
from django.db import models
UserModel = get_user_model()

class CategoryModel(models.Model):
    title = models.CharField(max_length=550,verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=_('created_at'))

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class GenderModel(models.Model):
    title = models.CharField(max_length=550,verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=_('created_at'))

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('gender')
        verbose_name_plural = _('genders')


class ColorsModel(models.Model):
    title = models.CharField(max_length=15, null=True, blank=True,verbose_name=_('title'))
    code = models.CharField(max_length=12,verbose_name=_('code'))
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=_('created_at'))

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('color')
        verbose_name_plural = _('colors')


class BrandModel(models.Model):
    title = models.CharField(max_length=550,verbose_name=_('title'))
    image = models.ImageField(upload_to='brands',verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=_('created_at'))

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name =_( 'brand')
        verbose_name_plural = _('brands')


class ProductTagModel(models.Model):
    title = models.CharField(max_length=550,verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=_('created_at'))

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class SizeModel(models.Model):
    title = models.CharField(max_length=3,verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=_('created_at'))

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('size')
        verbose_name_plural = _('sizes')


class ProductsModel(models.Model):
    title = models.CharField(max_length=550,verbose_name=_('title'))
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, related_name='products',verbose_name=_('category'))
    gender = models.ForeignKey(GenderModel, on_delete=models.PROTECT, related_name='product',verbose_name=_('gender'))
    price = models.FloatField(verbose_name=_('price'))
    brand = models.ForeignKey(BrandModel, on_delete=models.PROTECT, related_name='products',verbose_name=_('brand'))
    discount = models.PositiveIntegerField(default=0,verbose_name=_('discount'))
    description = models.TextField(verbose_name=_('description'))
    tags = models.ManyToManyField(ProductTagModel, related_name='products',verbose_name=_('tags'))
    model = models.CharField(max_length=30,verbose_name=_('model'))
    wishlist = models.ManyToManyField(UserModel, related_name='wishlist',verbose_name=_('wishlist'))
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=_('created_at'))
    real_price = models.FloatField(default=0,verbose_name=_('real_price'))
    sizes = models.ManyToManyField(SizeModel, related_name='products',verbose_name=_('sizes'))
    colors = models.ManyToManyField(ColorsModel, related_name='products',verbose_name=_('colors'))


    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')


    @staticmethod
    def get_from_cart(request):
        cart = request.session.get('cart', [])

        return ProductsModel.objects.filter(pk__in=cart)

    def get_image(self):
        images = self.images.all()
        if images:
            return self.images.first().image.url
        return '/static/img/noimage.png'

    def get_comments(self):
        return self.comments.order_by('-created_at')

    def is_discount(self):
        return self.discount != 0

    def get_price(self):
        if self.is_discount():
            return self.price - self.price * self.discount / 100
        return round(self.price, 2)

    def is_new(self):
        delta = datetime.now(pytz.timezone('Asia/Tashkent')) - self.created_at
        return delta.days <= 3


class ProductImageModel(models.Model):
    image = models.ImageField(upload_to='products',verbose_name=_('image'))
    product = models.ForeignKey(ProductsModel, on_delete=models.CASCADE, related_name='images',verbose_name=_('product'))

    def __str__(self):
        return f'{self.product.title}'

    class Meta:
        verbose_name = _('product image')
        verbose_name_plural = _('product images')


class CommentModel(models.Model):
    name = models.CharField(max_length=30,verbose_name=_('created_at'))
    email = models.EmailField(verbose_name=_('email'))
    comment = models.TextField(verbose_name=_('comment'))

    product = models.ForeignKey(ProductsModel, related_name='comments', on_delete=models.CASCADE,verbose_name=_('product'))

    created_at = models.DateTimeField(auto_now_add=True,verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
