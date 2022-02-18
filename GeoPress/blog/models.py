from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from auth2.models import User
from django.utils.timezone import now

class Article(models.Model):
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    post_pub_date = models.DateTimeField(auto_now_add=now, verbose_name='发布时间') # 文章发布时间
    post_mod_date = models.DateTimeField(default=now, verbose_name='修改时间') # 文章修改时间
    post_title = models.CharField(max_length=100, verbose_name='标题') # 文章标题 # CharField必须要指定max_length参数, 不指定会直接报错
    post_body = models.TextField(verbose_name='博文') # 文章正文
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, blank=True, null=True, verbose_name='分类') # 默认就与分类表的主键字段做外键关联
    tag = models.ManyToManyField(to='Tag', blank=True, verbose_name='标签') # 文章可以没有标签，因此为标签tag指定了blank=True

    # https://docs.djangoproject.com/zh-hans/4.0/ref/models/options/
    class Meta:
        # 设置模型的名字，但是记得复数形式也要设置，否则有些地方就变成 verbose_name + s 了
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self): # django admin下拉列表不显示值，显示为object的处理
        return self.post_title

class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name='分类名')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='标签名')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class ArticleUpDown(models.Model):
    like_author = models.ForeignKey(User, on_delete=models.CASCADE, null=True,verbose_name='评论作者')
    like_post = models.ForeignKey(to='Article', on_delete=models.CASCADE, null=True, verbose_name='评论文章')
    like_up = models.BooleanField(default=True, verbose_name='点赞')

    class Meta:
        unique_together = [
            ('like_author','like_post'),
        ] # 一组字段名，合起来必须是唯一的：
        verbose_name = '点赞'
        verbose_name_plural = verbose_name

class Comment(models.Model):
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='评论作者')
    comment_post = models.ForeignKey(to='Article', on_delete=models.CASCADE, verbose_name='评论文章')
    comment_pub_date = models.DateTimeField(auto_now_add=now, verbose_name='评论时间')
    comment_mod_date = models.DateTimeField(default=now, verbose_name='评论修改时间')
    comments = models.CharField(max_length=255, verbose_name='评论内容')
    # 父级评论：对文章的评论；子级评论：对评论的评论
    parent_comment = models.ForeignKey(to='self', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comments