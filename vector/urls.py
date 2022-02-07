from django.urls import path
from article.views import main, main_acricles, users_number, acricles_archive, users, article_number, article_number_archive, article_number_text



urlpatterns = [
    path('', main),
    path('acricles/', main_acricles, name='mail_acricles'),
    path('acrticles/archive', acricles_archive, name='mail_acrticles'),
    path('users/', users, name='users'),
    path('article/<int:article_id>/', article_number, name='article_number'),
    path('article/<int:article_id>/archive', article_number_archive, name='article_number'),
    path('article/<int:article_id>/<slug:slug_text>', article_number_text, name='article_number_text'),
    path('users/<int:users_id>/', users_number, name='users_number')


]