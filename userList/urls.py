from django.urls import path
from userList import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('<int:pk>', views.myPage, name='userList'),
]
