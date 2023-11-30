from django.contrib import admin
from django.urls import path
from core import views as core_views
from cursos import views as cursos_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='/home'),
    path('about/', core_views.about),
    path('contact/', core_views.contact),
    path('cursos/', cursos_views.cursos),
]
  #  path('Post/', post_views.post_list, name='Post'),
   # path('about/', core_views.about),
    #path('ranking/', core_views.ranking),


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)