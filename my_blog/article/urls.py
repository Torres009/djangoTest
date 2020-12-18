# 2020.10.10新增代码 引入path,view

from django.urls import path
from . import views

# 2020.10.10新增代码 APP名称

app_name = 'article'

# 2020.10.10新增代码 APP子路径
urlpatterns = [
    # 当前为空
    # path('',views.HelloWorld, name = 'HelloWorld'),
    path('article-list/', views.article_list, name='article_list'),

    # 文章详情
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),

    path('article-create/', views.article_create, name='article_create'),

    path('article-safe-delete/<int:id>/', views.article_safe_delete,
         name='article_safe_delete'),
]
