
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rating.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('Restaurent', RestaurentViewSet, basename='Restaurent')
router.register('Rating', RatingViewSet, basename='Rating')
router.register('Staff', StaffViewSet, basename='Staff')
router.register('StaffSalary', StaffSalaryViewSet, basename='Staffsalary')
router.register('Sales', SalesViewSet, basename='Sales')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))

] 
