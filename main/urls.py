from django.urls import path
from main import views
from django.conf.urls.static import static
from django.conf import settings
from .views import BasePageView, PostPageView

urlpatterns = [
    path('', BasePageView.as_view(), name='mainPage'),
    path('post/<int:pk>', PostPageView.as_view(), name='postPage'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
