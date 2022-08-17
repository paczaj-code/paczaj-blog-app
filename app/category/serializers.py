from faulthandler import is_enabled
from rest_framework import serializers
from collections import OrderedDict
from .models import Category
from blog.models import Post


class BasicCategorySerializer(serializers.ModelSerializer):
    """Serializer template for categories to be inherited"""
    posts = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'icon', 'slug', 'posts']

    def to_representation(self, instance):
        """Clean of empty values and add count of subcategories"""
        result = super(BasicCategorySerializer,
                       self).to_representation(instance)
        result['subcount'] = instance.subcategories.count()
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None and result[key] != []])

    def get_posts(self, obj):
        """Add field post as count of related articles"""
        posts = Post.objects.filter(category_id__in=[obj]).count()
        return posts


class PublicCategoryListSerializer(BasicCategorySerializer):
    """Serilazer for category list API with recursive subcategories"""
    class Meta:
        model = Category
        fields = BasicCategorySerializer.Meta.fields

    def get_fields(self):
        fields = super(PublicCategoryListSerializer, self).get_fields()
        fields['subcategories'] = PublicCategoryListSerializer(many=True)
        # fields = Category.objects.filter(is_enabled=True)
        return fields

    # def get_subcategories(self, obj):
    #     queryset = Category.objects.filter(subcategory__is_enabled=True)
    #     return PublicCategoryDetailSerializer(queryset, many=True)


class PublicCategoryDetailSerializer(BasicCategorySerializer):
    """Serializer for category detail API """
    class Meta:
        model = Category
        fields = BasicCategorySerializer.Meta.fields + ['description']
