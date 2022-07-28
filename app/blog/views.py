from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .serializers import (PublicCategoryListSerializer, PublicCategoryDetailSerializer,
                          PostsListByCategorySerializer, PostDetailByPostIdOrSlug)
from .models import Category, Post
from django.db.models import Q
from rest_framework import generics


class CategoryListAPIView(APIView):
    """View for category lists with recursive subcategories"""

    def get(self, request, *args, **kwargs):
        # TODO resolve problem with filtering by is_enebled in subcategories
        categories = Category.objects.filter(category_type='P',
                                             is_enabled=True, parent__isnull=True)
        serializer = PublicCategoryListSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryDetailAPIViewByPkOrSlug(APIView):
    """View for category details"""

    def get_object_by_pk(self, pk):
        try:
            return Category.objects.get(pk=pk, is_enabled=True, category_type='P',)
        except Category.DoesNotExist:
            raise Http404

    def get_object_by_slug(self, slug):
        try:
            return Category.objects.get(slug=slug, is_enabled=True, category_type='P',)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        slug = self.kwargs.get('slug', None)
        if pk:
            obj = self.get_object_by_pk(pk)
        else:
            obj = self.get_object_by_slug(slug)
        serializer = PublicCategoryDetailSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostListAPIViewByCategoryIdOrSlug(APIView):
    """View for posts list with category data"""

    def get_objects_by_pk(self, pk):
        try:
            posts = Post.objects.filter(category_id=pk, is_published=True)
            category = Category.objects.get(
                pk=pk, is_enabled=True, category_type='P',)
            obj = {'posts': posts, 'category': category}
            return obj
        except Category.DoesNotExist:
            raise Http404

    def get_objects_by_slug(self, slug):
        try:
            posts = Post.objects.filter(
                category__slug=slug, is_published=True)
            category = Category.objects.get(
                slug=slug, is_enabled=True, category_type='P',)
            obj = {'posts': posts, 'category': category}
            return obj
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        slug = self.kwargs.get('slug', None)
        # post = self.get_object(pk)
        if pk:
            obj = self.get_objects_by_pk(pk)
        else:
            obj = self.get_objects_by_slug(slug)
        serializer = PostsListByCategorySerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostDetailAPIViewByPostIdOrSlug(APIView):
    def get_objects_by_pk(self, pk):
        try:
            post = Post.objects.get(pk=pk, is_published=True)
            category = Category.objects.get(
                id=post.category.id, is_enabled=True)
            obj = {'post': post, 'category': category}
            return obj
        except Post.DoesNotExist:
            raise Http404

    def get_objects_by_slug(self, slug):
        try:
            post = Post.objects.get(
                slug=slug, is_published=True)
            category = Category.objects.get(
                id=post.category.id, is_enabled=True)
            obj = {'post': post, 'category': category}
            return obj
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        slug = self.kwargs.get('slug', None)
        if pk:
            obj = self.get_objects_by_pk(pk)
        else:
            obj = self.get_objects_by_slug(slug)
        serializer = PostDetailByPostIdOrSlug(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
