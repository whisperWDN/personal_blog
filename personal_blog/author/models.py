from django.db import models
from uuid import uuid4


# Create your models here.
class Author(models.Model):
    GENDER = {
        '0': '女',
        '1': '男',
    }
    STATUS = {
        '0': '正常',
        '1': '锁定',
        '2': '删除'
    }
    # 作者编号
    # id = models.AutoField(primary_key=True, verbose_name='作者编号')
    id = models.UUIDField(primary_key=True, verbose_name='作者编号', auto_created=True, default=uuid4)
    # 登陆账号
    username = models.CharField(max_length=50, verbose_name='登陆账号', unique=True, db_index=True)
    # 登陆密码'
    password = models.CharField(max_length=50, verbose_name='登陆密码')
    # 真实姓名
    realname = models.CharField(max_length=20, verbose_name='作者姓名', default='待完善', null=True, blank=True, db_index=True)
    # 用户昵称
    nickname = models.CharField(max_length=20, verbose_name='作者昵称', default='待完善', null=True, blank=True, db_index=True)
    # 年龄
    age = models.IntegerField(default=0, verbose_name='作者年龄')
    # 性别
    gender = models.CharField(max_length=1, choices=GENDER, verbose_name='用户性别', null=True, blank=True)
    # 邮箱
    email = models.CharField(verbose_name="联系邮箱", null=True, blank=True, db_index=True)
    # 电话
    phone = models.CharField(max_length=20, verbose_name="联系电话", null=True, blank=True, db_index=True)
    # 用户状态
    status = models.CharField(max_length=5, choices=STATUS, verbose_name='用户状态', help_text='必须选择其中一个状态')
    # 注册时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="注册时间")
    # 修改时间
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    # 个人主页
    personal_page = models.URLField(verbose_name='个人主页', null=True, blank=True)
    # 个人介绍
    intro = models.TextField(verbose_name='个人介绍')
    # 备注信息
    remark = models.TextField(verbose_name='备注信息')
    # 喜欢的文章
    articles_liked = models.ManyToManyField('article.Article', related_name='articleliked')
    # 收藏的文章
    articles_collected = models.ManyToManyField('article.Article', related_name='articlecollected')
    # 喜欢的作者
    authors_liked = models.ManyToManyField('self', related_name='author')
    # 特别喜欢的作者
    authors_liked  = models.OneToOneField('self', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = '作者'

    def __str__(self):
        return '账号:{};昵称:{};姓名:{}'.format(self.username, self.nickname, self.realname)


class AuthorProfile(models.Model):
    # 编号
    id = models.UUIDField(primary_key=True, verbose_name='扩展资料编号', auto_created=True, default=uuid4)
    # 粉丝数量
    fans_count = models.IntegerField(verbose_name='粉丝数量', default=0)
    # 访问数量
    visited_count = models.IntegerField(verbose_name='访问数量', default=0)
    # 文章字数
    words_count = models.IntegerField(verbose_name='文章字数', default=0)
    # 文章篇数
    article_count = models.IntegerField(verbose_name='文章篇数', default=0)
    # 收藏总数
    collected_count = models.IntegerField(verbose_name='收藏总数', default=0)
    # 喜欢总数
    liked_count = models.IntegerField(verbose_name='喜欢总数', default=0)
    # 点赞总数
    admired_count = models.IntegerField(verbose_name='点赞总数', default=0)
    # 关联用户
    author = models.OneToOneField(Author, on_delete=models.CASCADE)