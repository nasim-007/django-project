
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve as mediaserve





urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('blog.urls', namespace='blog')),
    
    path('carousel/', include('carousel.urls', namespace='carousel')),
    path('myapp/', include('myapp.urls', namespace='myapp')),
    path('album/', include('album.urls', namespace='album')),
    path('summernote/', include('django_summernote.urls'))


]


urlpatterns.append(url(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
                     mediaserve, {'document_root': settings.MEDIA_ROOT}))

urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)