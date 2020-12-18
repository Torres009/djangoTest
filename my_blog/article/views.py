from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect

# 引入刚才定义的ArticlePostForm表单类
from .froms import ArticlePostForm
# 引入User模型
from django.contrib.auth.models import User

# # def HelloWorld(request):
# #     return HttpResponse("Hello world!")
#
# # Create your views here.
# # 导入我们的数据类ArticlePost
from .models import ArticlePost

def article_list(request):
    articles = ArticlePost.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'article/list.html', context)

#	注意是是增加，不要把之前的article_list函数删除了
#   显示文章详情
def article_detail(request, id):
    #   取出相应文章
    article = ArticlePost.objects.get(id=id)
    #   需要传递给模板的对象
    context = {'article':article}
    #   载入模板，返回context对象
    return render(request, 'article/detail.html',context)

# 写文章的视图
def article_create(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            # 指定数据库中 id=1 的用户为作者
            # 如果你进行过删除数据表的操作，可能会找不到id=1的用户
            # 此时请重新创建用户，并传入此用户的id
            new_article.author = User.objects.get(id=1)
            # 将新文章保存到数据库中
            new_article.save()
            # 完成后返回到文章列表
            return redirect("article:article_list")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文
        context = { 'article_post_form': article_post_form }
        # 返回模板
        return render(request, 'article/create.html', context)

# 删除文章
def article_safe_delete(request, id):
    if request.method == 'POST':
        article = ArticlePost.objects.get(id=id)
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("仅允许POST请求删除文章")

