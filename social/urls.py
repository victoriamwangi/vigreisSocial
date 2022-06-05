from django.urls import re_path 
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    re_path('^$', views.home, name= "home"),
    re_path('^new/post$', views.new_post, name= "new_post"),
    re_path('^profile', views.profile, name = "profile"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)