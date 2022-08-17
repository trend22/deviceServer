"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# create obj of routers
from rest_framework import routers

from devices.views import *

router = routers.SimpleRouter()
# # create url for router and view
router.register(r'api/v1/devices', DeviceViewSet)
router.register(r'api/v1/companyuse', CompanyUseViewSet)
router.register(r'api/v1/classofdevice', ClassOfDeviceViewSet)
router.register(r'api/v1/interval', IntervalCheckViewSet)
router.register(r'api/v1/companycheck', CompanyCheckViewSet)
router.register(r'api/v1/typeofsi', TypeOfSiViewSet)
router.register(r'api/v1/sichecks', SiCheckViewSet)
router.register(r'api/v1/iochecks', IoCheckViewSet)
router.register(r'api/v1/indicatorchecks', IndicatorCheckViewSet)
router.register(r'api/v1/skchecks', SkCheckViewSet)
router.register(r'api/v1/allchecks', AllCheckAPIView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-server/', include('rest_framework.urls')),
    path('users/', include('users.urls')),
]

# add url to urlpatters
urlpatterns += router.urls
