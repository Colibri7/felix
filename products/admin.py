
from django.contrib import admin
from django import forms
from modeltranslation.admin import TranslationAdmin

from products.models import ProductsModel, CategoryModel, BrandModel, ProductTagModel, SizeModel, ProductImageModel, \
    CommentModel, GenderModel, ColorsModel


class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



@admin.register(CategoryModel)
class CategoryAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(GenderModel)
class GenderAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


class ColorForm(forms.ModelForm):
    class Meta:
        model = ColorsModel
        fields = '__all__'
        widgets = {
            'code': forms.TextInput(attrs={'type': 'color'}),
        }


@admin.register(ColorsModel)
class ColorsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']
    form = ColorForm


@admin.register(BrandModel)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(ProductTagModel)
class ProductTagAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


class ProductImageModelAdmin(admin.TabularInline):
    model = ProductImageModel


@admin.register(ProductsModel)
class ProductAdmin(MyTranslationAdmin):
    list_display = ['title', 'category', 'brand', 'price', 'discount', 'created_at']
    search_fields = ['title', 'category__title', 'description']
    list_filter = ['category', 'brand', 'tags', 'created_at']
    autocomplete_fields = ['category', 'brand', 'tags', 'sizes']
    readonly_fields = ['real_price']

    inlines = [ProductImageModelAdmin]

    def change_view(self, request, **kwargs):
        self.exclude = ('wishlist',)
        return super().change_view(request, **kwargs)


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'product']
    list_filter = ['product', 'created_at']
    search_fields = ['name', 'email']
