from django.urls import path
from .views import PostList, PostDetail, NewsCreate,NewsUpdate,\
    NewsDelete,ArticleCreate,ArticleUpdate,ArticleDelete,NewsSearch

urlpatterns = [
    path('', PostList.as_view(),name='post_list'),
    path('<int:pk>', PostDetail.as_view(),name='post_detail'),
    path('search/', NewsSearch.as_view(),name='news_search'),
    path('create/', NewsCreate.as_view(),name='news_create'),
    path('create/', ArticleCreate.as_view(),name='article_create'),
    path('<int:pk>/update/',NewsUpdate.as_view(),name='news_update'),
    path('<int:pk>/update/',ArticleUpdate.as_view(),name='article_update'),
    path('<int:pk>/delete/',NewsDelete.as_view(),name='news_delete'),
    path('<int:pk>/delete/',ArticleDelete.as_view(),name='article_delete'),

]