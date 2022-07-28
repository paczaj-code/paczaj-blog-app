from rest_framework import serializers
from collections import OrderedDict
from blog.models import Category, Tag, Post

"""-----------------Category serializers begin----------------------"""


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
        return fields


class PublicCategoryDetailSerializer(BasicCategorySerializer):
    """Serializer for category detail API """
    class Meta:
        model = Category
        fields = BasicCategorySerializer.Meta.fields + ['description']


"""-----------------Category serializers end----------------------"""

"""-----------------Tag serializers begin----------------------"""


class TagSerializer(serializers.ModelSerializer):
    """Tag serializer for Post serializers"""
    class Meta:
        model = Tag
        fields = ['name', 'icon']


"""-----------------Tag serializers end----------------------"""

"""-----------------Post serializers begin ----------------------"""


class BasicPostSerializer(serializers.ModelSerializer):
    """Serializer template for post to be inherited"""
    created_at = serializers.DateTimeField(format='%d-%m-%Y')
    modified_at = serializers.DateTimeField(format='%Y')
    tag = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'slug', 'created_at',
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


"""-----------------Post serializers end ----------------------"""