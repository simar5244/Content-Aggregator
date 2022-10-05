from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('content1/', updatepython,name='update1'),
    path('content2/', updateprog,name='update2'),
    path('content3/', updatecovid,name='update3'),
    path('content4/', updatehiring,name='update4'),
]
 
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
