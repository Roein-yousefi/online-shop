from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from django.urls import reverse


class ActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentManager , self).get_queryset().filter(active=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    datetime_added = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail' , args={self.id})


class Comment(models.Model):
    PRODUCT_CHOICES = [
        ('1' , _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('1', _('Good')),
        ('1', _('Perfect')),
    ]
    product = models.ForeignKey(Product ,on_delete=models.CASCADE ,related_name='comments')
    text = models.TextField(verbose_name=_('comment'))

    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE ,related_name='comments')
    stars = models.CharField(max_length=10 ,choices=PRODUCT_CHOICES ,verbose_name=_('what is your score?'))


    datetime_added = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    #manager
    object = models.Manager()
    comments_active_manager = ActiveCommentManager()