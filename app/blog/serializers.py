from rest_framework import serializers
from collections import OrderedDict
from blog.models import Tag, Post
from category.serializers import PublicCategoryDetailSerializer


"""-----------------Tag serializers begin----------------------"""


class TagSerializer(serializers.ModelSerializer):
    """Tag serializer for Post serializers"""
    class Meta:
        model = Tag
        fields = ['name', 'icon']

    def to_representation(self, instance):
        """Clean of empty values and add count of subcategories"""
        result = super(TagSerializer,
                       self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None and result[key] != ""])


"""-----------------Tag serializers end----------------------"""

"""-----------------Post serializers begin ----------------------"""


class BasicPostSerializer(serializers.ModelSerializer):
    """Serializer template for post to be inherited"""
    created_at = serializers.DateTimeField(format='%d-%m-%Y')
    modified_at = serializers.DateTimeField(format='%d-%m-%Y')
    tag = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'created_at',
                  'modified_at', 'tag']

    def to_representation(self, instance):
        """Clean of empty values and add count of subcategories"""
        result = super(BasicPostSerializer,
                       self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None and result[key] != ""])


class DetailPostSerializer(BasicPostSerializer):
    """Serialzer for  post details view """
    class Meta:
        model = Post
        fields = BasicPostSerializer.Meta.fields + \
            ['content', 'demo_css', 'demo_js']


class PostsListByCategorySerializer(serializers.Serializer):
    """Serialzer for post list by category id or slug with category data"""
    posts = BasicPostSerializer(many=True)
    category = PublicCategoryDetailSerializer(read_only=True)

    class Meta:
        fields = ['posts', 'category']


class PostDetailByPostIdOrSlug(serializers.Serializer):
    post = DetailPostSerializer()
    category = PublicCategoryDetailSerializer(read_only=True)

    class Meta:
        fields = ['post', 'category']


# """-----------------Post serializers end ----------------------"""


# TODO dodać obrazki przy zapisywaniu
