from django.urls import path
from .views import TermListAPIView, TermDetailAPIViewByPK, TermDetailAPIViewBySlug


urlpatterns = [
    path('term/', TermListAPIView.as_view()),
    path('term/<int:pk>/', TermDetailAPIViewByPK.as_view()),
    path('term/<str:slug>/', TermDetailAPIViewBySlug.as_view()),

]
