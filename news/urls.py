from django.urls import path, include
from .views import PostList, PostDetail, NewsSearch, NewsCreate, NewsUpdate, NewsDelete, upgrade_me, CategoryListView, \
    subscribe, IndexView
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('',cache_page(60*10)(PostList.as_view()), name='post_list'),
    path('<int:pk>',cache_page(60*10)(PostDetail.as_view()), name='post_detail'),
    path('search/', NewsSearch.as_view(), name='post_search'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/create/', NewsCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', NewsUpdate.as_view(), name='articles_edit'),
    path('articles/<int:pk>/delete/', NewsDelete.as_view(), name='articles_delete'),
    path('upgrade/', upgrade_me, name='upgrade'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
    path('protect/', IndexView.as_view()),



]