from django.conf.urls import include, url


urlpatterns = [
    url(r'^', include('applications.home.urls')),
    url(r'^api/', include('applications.post_comment.urls')),
]