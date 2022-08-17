from django.urls import path
from .views import (PractiseListAPIViewByCategoryIdOrSlug,
                    PractiseDetailView, ExerciseView)

urlpatterns = [
    # endpoint for post list by category id
    path('practices/<int:pk>', PractiseListAPIViewByCategoryIdOrSlug.as_view(),
         name='practices-by-category-id'),
    path('practices/<str:slug>', PractiseListAPIViewByCategoryIdOrSlug.as_view(),
         name='practices-by-category-slug'),
    path('practice/<int:pk>', PractiseDetailView.as_view(),
         name='practice-by-id'),
    path('practice/<str:slug>', PractiseDetailView.as_view(),
         name='practice-by-slug'),
    path('practice/<str:slug>/<int:number>', ExerciseView.as_view(),
         name='practice-by-slug'),
    # endpoint for post list by category slug
    # path('posts/<str:slug>', PostListAPIViewByCategoryIdOrSlug.as_view(),
    #      name='post-by-category-slug'),
    # path('post/<int:pk>', PostDetailAPIViewByPostIdOrSlug.as_view(),
    #      name='post-by-id'),
    # # endpoint for post list by category slug
    # path('post/<str:slug>', PostDetailAPIViewByPostIdOrSlug.as_view(),
    #      name='post-by-slug'),
]

app_name = 'practice'
