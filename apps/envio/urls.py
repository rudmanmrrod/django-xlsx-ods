from django.conf.urls import url
from .views import index,envioUpload

urlpatterns = [
    url(r'^$', index.as_view(),name='index'),
    url(r'^upload_file$', envioUpload.as_view(),name='upload_file'),
]