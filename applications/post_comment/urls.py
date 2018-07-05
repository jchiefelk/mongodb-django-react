from django.conf.urls import url
from rest_framework import routers
from . import views


# router = routers.DefaultRouter()
# router.register(r'data', views.snippet_list, base_name="api")

urlpatterns = [
   url(r'^data/$', views.snippet_list),
]