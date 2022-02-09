from django.urls import path
from article.views import index, first,  main_acricles, users_number,  users, article_number, article_number_archive, article_number_slug, random_slug, random_page



urlpatterns = [
    path('', index, name='main'),
    path('first', first, name='first'),
    path('acricles/', main_acricles, name='main_acricles'),
    path('users/', users, name='users'),
    path('article/<int:article_id>/', article_number, name='article_number'),
    path('article/<int:article_id>/archive', article_number_archive, name='article_number'),
    path('article/<int:article_id>/<slug:slug_text>', article_number_slug, name='article_number_slug'),
    path('users/<int:users_id>/', users_number, name='users_number'),
    path('random_page/', random_page, name='random_page'),
    path('random_slug/', random_slug, name='random_slug'),


]