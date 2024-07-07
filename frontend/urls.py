from django.urls import path,re_path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',IndexView,name='index')
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)