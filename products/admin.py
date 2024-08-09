from django.contrib import admin

from .models import Product , Comment


class CommentsInline(admin.TabularInline):
    model = Comment
    fields = ['author','text' , 'active' , 'stars']

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name' , 'price', 'active')

    inlines = [CommentsInline]


admin.site.register(Product, ProductAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author' , 'product','text' , 'active' , 'stars')

admin.site.register(Comment, CommentAdmin)
