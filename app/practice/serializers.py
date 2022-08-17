from dataclasses import fields
from rest_framework import serializers
from collections import OrderedDict
from .models import Practice, Exercise
from category.serializers import PublicCategoryDetailSerializer
from blog.models import Post


class RelatedPostsSerializer(serializers.ModelSerializer):
    """Tag serializer for Post serializers"""
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug']


class RelatedExercises(serializers.ModelSerializer):
    """Serializer for"""
    class Meta:
        model = Exercise
        fields = ['id', 'number', 'difficulty']


class BasePractiseSerializer(serializers.ModelSerializer):
    num_exer = serializers.SerializerMethodField()

    class Meta:
        model = Practice
        # fields = ['id', 'title', 'slug', 'category',
        #           'modified_at', 'created_at']
        fields = ['id', 'title', 'slug',
                  'created_at', 'modified_at', 'num_exer']

    def get_num_exer(self, obj):
        exer = Exercise.objects.filter(practise=obj).count()
        return exer


class PractiseListByCategoryIdOrSlug(serializers.Serializer):
    """Serialzer for post list by category id or slug with category data"""
    practice = BasePractiseSerializer(many=True)
    category = PublicCategoryDetailSerializer(read_only=True)

    class Meta:
        fields = ['practice', 'category']


class PractiseDetailByIdOrSlug(serializers.ModelSerializer):
    related_posts = RelatedPostsSerializer(many=True, read_only=True)
    # related_exer = RelatedExercises(many=True, read_only=True)
    related_exer = serializers.SerializerMethodField()

    class Meta:
        model = Practice
        fields = ['id', 'title', 'created_at', 'modified_at',
                  'related_posts', 'related_exer']

    def get_related_exer(self, obj):
        rel = Exercise.objects.filter(practise_id=obj)
        # return rel
        return RelatedExercises(rel, many=True).data


class ExersiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = ['id', 'number', 'difficulty', 'exercise', 'solution']


# TODO Refactoring i dodac daty i testy
