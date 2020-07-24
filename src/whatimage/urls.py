
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from images.admin import adminSite 

urlpatterns = [
    path('admin/', adminSite.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/',include('images.api.urls',namespace='api-images'))

]

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
