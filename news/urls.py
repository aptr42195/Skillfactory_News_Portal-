from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
<<<<<<< HEAD
from .views import PostList, PostDetail, NewsCreate, NewsUpdate, \
    NewsDelete, ArticleCreate, ArticleUpdate, ArticleDelete, NewsSearch, BaseRegisterView, IndexView, upgrade_me

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),#
    path('news/<int:pk>', PostDetail.as_view(), name='post_detail'),#
    path('news/search/', NewsSearch.as_view(), name='news_search'),#
    path('news/create/', NewsCreate.as_view(), name='news_create'),#
    path('news/article/create/', ArticleCreate.as_view(), name='article_create'),
    path('news/<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),#
    path('news/<int:pk>/update/', ArticleUpdate.as_view(), name='article_update'),#
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),#
    path('news/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),#
    path('news/protect/',IndexView.as_view(template_name = 'sign/protect.html'),name='protect'),
    path('news/upgrade/', upgrade_me, name='upgrade'),
    # path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    # path('news/login/',LoginView.as_view(template_name = 'sign/login.html')),
    path('news/login/',
         LoginView.as_view(template_name='sign/login.html'),
         name='login'),
    path('news/logout/',
         LogoutView.as_view(template_name='sign/logout.html'),
         name='logout'),
    path('news/signup/',
         BaseRegisterView.as_view(template_name='sign/sign.html'),
         name='sign'),
]
=======
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
>>>>>>> 8dc332dc15bc6b6b2a0e0bca3cad4c6cd45214fd
