from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django_app.views import JihazAPIList, JihazAPIDestroy, JihazAPIUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('django_app.urls')),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/jihaz', JihazAPIList.as_view()),
    path('api/v1/jihaz/<int:pk>/', JihazAPIUpdate.as_view()),
    path('api/v1/jihazdelete/<int:pk>/', JihazAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path('r^auth/', include('djoser.urls.authtoken')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

