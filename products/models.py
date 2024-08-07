from django.db import models
from django.contrib.auth import get_user_model

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
        ('1' , 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Normal'),
        ('1', 'Good'),
        ('1', 'Perfect'),
    ]


    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='comments')
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE , related_name='comments')
    stars = models.CharField(max_length=10 , choices=PRODUCT_CHOICES)

    datetime_added = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    #manager
    object = models.Manager()
    comments_active_manager = ActiveCommentManager()