from django.contrib import admin

# Register your models here.

# 注册ArticlePost
# 我们之前建立了ArticlePost模型类，也进行了数据迁移，不过虽然有了这个模型类，
# 我们在后台里面还没法管理它，需要把它注册到管理员后台。

from .models import ArticlePost
# 注册ArticlePost
admin.site.register(ArticlePost)
