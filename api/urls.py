

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import employeeViewSet


router = routers.DefaultRouter()
router.register(r'employees', employeeViewSet)
urlpatterns = [
    path('', include(router.urls))

]
