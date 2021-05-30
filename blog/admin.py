from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Category
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}



class PostAdmin(SummernoteModelAdmin):

    list_display = [
        'title',
        'short_description',
        'description',
        'thumbnail',
        
    ]

    summernote_fields = ('description',)

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'body'
      
    ]

admin.site.register(Comment, CommentAdmin)


'''
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

'''