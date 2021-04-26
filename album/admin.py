from django.contrib import admin


from .models import Album
# Register your models here.

class AlbumAdmin(admin.ModelAdmin):

    list_display = [
        'description',
        'thumbnail',
        'creation'
       
    ]

admin.site.register(Album, AlbumAdmin)