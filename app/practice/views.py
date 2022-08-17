from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .serializers import(PractiseListByCategoryIdOrSlug,
                         PractiseDetailByIdOrSlug, ExersiceSerializer)
from category.models import Category
from .models import Practice, Exercise


class PractiseListAPIViewByCategoryIdOrSlug(APIView):
    """View for posts list with category data"""

    def get_objects_by_pk(self, pk):
        try:
            practice = Practice.objects.filter(
                category_id=pk, is_published=True)
            category = Category.objects.get(
                pk=pk, is_enabled=True, category_type='E')
            obj = {'practice': practice, 'category': category}
            return obj
        except Category.DoesNotExist:
            raise Http404

    def get_objects_by_slug(self, slug):
        try:
            practice = Practice.objects.filter(
                category__slug=slug, is_published=True)
            category = Category.objects.get(
                slug=slug, is_enabled=True, category_type='E')
            obj = {'practice': practice, 'category': category}
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
        serializer = PractiseListByCategoryIdOrSlug(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PractiseDetailView(APIView):
    def get_objects_by_pk(self, pk):
        try:
            return Practice.objects.get(
                pk=pk, is_published=True)
        except Practice.DoesNotExist:
            raise Http404

    def get_objects_by_slug(self, slug):
        try:
            return Practice.objects.get(
                slug=slug, is_published=True)
        except Practice.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        slug = self.kwargs.get('slug', None)
        if pk:
            obj = self.get_objects_by_pk(pk)
        else:
            obj = self.get_objects_by_slug(slug)
        serializer = PractiseDetailByIdOrSlug(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ExerciseView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            number = self.kwargs.get('number', None)
            slug = self.kwargs.get('slug', None)
            practise = Practice.objects.get(slug=slug)
            exercise = Exercise.objects.get(number=number,
                                            practise=practise, is_published=True)
            serializer = ExersiceSerializer(exercise)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exercise.DoesNotExist:
            raise Http404
