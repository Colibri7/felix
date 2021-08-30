from rest_framework import serializers

from products.models import ProductsModel, CategoryModel, BrandModel, SizeModel, ColorsModel, ProductTagModel


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        exclude = ['title_ru', 'title_en', ]


class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = '__all__'


class SizeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeModel
        fields = '__all__'


class TagsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTagModel
        exclude = ['title_ru', 'title_en', ]


class ColorsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorsModel
        fields = '__all__'


class ProductsModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer()
    brand = BrandModelSerializer()
    sizes = SizeModelSerializer(many=True)
    colors = ColorsModelSerializer(many=True)
    tags = TagsModelSerializer(many=True)

    class Meta:
        model = ProductsModel
        exclude = ['title_ru', 'title_en', 'description_en', 'description_ru', 'wishlist']
