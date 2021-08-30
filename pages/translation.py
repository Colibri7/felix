from modeltranslation.translator import register, TranslationOptions

from pages.models import HomeModel


@register(HomeModel)
class HomeModelTranslationOptions(TranslationOptions):
    fields = ('title_1', 'title_2',)

