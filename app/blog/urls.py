# from django.urls import path
# from .views import (CategoryListAPIView, CategoryDetailAPIViewByPkOrSlug,
#                     PostListAPIViewByCategoryIdOrSlug, PostDetailAPIViewByPostIdOrSlug)

# urlpatterns = [
#     # endpoint for categpry list
#     path('category/', CategoryListAPIView.as_view(), name='category-list'),
#     # endpoint for categpry detail by category id
#     path('category/<int:pk>', CategoryDetailAPIViewByPkOrSlug.as_view(),
#          name='category-by-id'),
#     # endpoint for categpry detail by category slug
#     path('category/<str:slug>', CategoryDetailAPIViewByPkOrSlug.as_view(),
#          name='category-by-slug'),
#     # endpoint for post list by category id
#     path('posts/<int:pk>', PostListAPIViewByCategoryIdOrSlug.as_view(),
#          name='post-by-category-id'),
#     # endpoint for post list by category slug
#     path('posts/<str:slug>', PostListAPIViewByCategoryIdOrSlug.as_view(),
#          name='post-by-category-slug'),
#     path('post/<int:pk>', PostDetailAPIViewByPostIdOrSlug.as_view(),
#          name='post-by-id'),
#     # endpoint for post list by category slug
#     path('post/<str:slug>', PostDetailAPIViewByPostIdOrSlug.as_view(),
#          name='post-by-slug'),
# ]

# app_name = 'blog'
