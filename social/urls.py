from django.urls import re_path , path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    re_path('^$', views.home, name= "home"),
    re_path('^new/post$', views.new_post, name= "new_post"),
    re_path('^profile$', views.profile, name = "profile"),
    re_path('^update_profile$', views.update_profile, name= "update_profile"),
    # re_path('^like_post/post_id', views.like_post, name = "like_post", )
    # re_path('^search_profile', views.search_profile, name='search_profile' ),
    re_path(r'^like/(?P<operation>.+)/(?P<pk>\d+)/',views.like, name='like'),
    re_path(r'^user/(?P<username>\w+)$', views.ShowUserPage)
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)