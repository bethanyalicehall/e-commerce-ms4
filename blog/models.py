from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    article_id = models.ForeignKey('Post', null=True,
                                   related_name="comments", blank=True,
                                   on_delete=models.SET_NULL)
    user_id = models.ForeignKey(User, null=True,
                                blank=True, on_delete=models.SET_NULL)
    comment_title = models.CharField(max_length=50)
    comment_content = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True,
                                      verbose_name='comment_created_date')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return '{}, {}, {}'.format(self.article_id,
                                   self.user_id,
                                   self.comment_title)