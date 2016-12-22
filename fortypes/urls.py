"""fortypes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from accounts.views import InviteCodeRegisterView
from fonts.views import FileUploadView, FontCountView, FontViewSet
from user_font_relation.views import UserFontRelationsViewSet

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/font_upload/(?P<filename>[^/]+)$', FileUploadView.as_view(), name='font-upload'),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api/invite-registration/', InviteCodeRegisterView.as_view(), name='invite-registration')
]

router = DefaultRouter()
router.register(r'api/fonts/', FontViewSet, base_name='fonts')
router.register(r'api/fonts-count/', FontCountView, base_name='fonts-count')
router.register(r'api/fonts-relations/', UserFontRelationsViewSet, base_name='fonts-relations')


urlpatterns += router.urls
