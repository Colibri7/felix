from products.models import GenderModel, CategoryModel, ProductsModel, ProductTagModel
from modeltranslation.translator import register, TranslationOptions

@register(CategoryModel)
class CategoryModelTranslationOptions(TranslationOptions):
    fields = ('title', )

@register(GenderModel)
class GenderModelTranslationOptions(TranslationOptions):
    fields = ('title', )

@register(ProductsModel)
class ProductsModelTranslationOptions(TranslationOptions):
    fields = ('title','description', )


@register(ProductTagModel)
class ProductTagModelTranslationOptions(TranslationOptions):
    fields = ('title',)

