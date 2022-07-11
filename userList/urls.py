from django.urls import path
from userList import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('<int:pk>', views.myPage, name='userList'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
