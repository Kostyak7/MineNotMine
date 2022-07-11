from django.urls import path
from main import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.basePage, name='mainPage'),
    path('post/<int:pk>', views.postPage, name='postPage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
