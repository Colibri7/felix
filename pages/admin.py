from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from pages.models import ContactModel, HomeModel


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


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'text', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'phone', 'text']


@admin.register(HomeModel)
class HomeModelAdmin(MyTranslationAdmin):
    list_display = ['id', 'title_1', 'title_2']
    list_filter = ['created_at']
