from django.db import models
from uuid import uuid4


# Create your models here.
class Article(models.Model):

    ARTICLE_STATUS = (
        ('0', '正常'),
        ('1', '删除')
    )
    # 编号
    id = models.UUIDField(primary_key=True, verbose_name='文章编号', auto_created=True, default=uuid4)
    # 标题
    title = models.CharField(max_length=200, verbose_name='文章标题')
    # 内容
    content = models.TextField(verbose_name='文章内容')
    # 发布时间
    pub_time = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    # 阅读次数
    readed_count = models.IntegerField(verbose_name='阅读次数', default=0)
    # 点赞次数
    admired_count = models.IntegerField(verbose_name='点赞次数', default=0)
    # 喜欢次数
    liked_count = models.IntegerField(verbose_name='喜欢次数', default=0)
    # 收藏次数
    collected_count = models.IntegerField(verbose_name='收藏次数', default=0)
    # 评论次数
    commented_count = models.IntegerField(verbose_name='评论次数', default=0)
    # 修改时间
    up_time = models.DateTimeField(auto_now=True, verbose_name="上次修改时间")
    # 文章状态
    status = models.CharField(verbose_name='当前状态', choices=ARTICLE_STATUS, default='0')
    # 文章作者
    author = models.ForeignKey('author.Author', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pub_time', 'id']

    def __str__(self):
        return "文章标题:{}, 文章内容:{}, ".format(self.title, self.content)
