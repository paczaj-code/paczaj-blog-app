from django.shortcuts import render

# Create your views here.


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
