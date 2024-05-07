from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('user-orders', views.UserOrderViewSet, basename='user-orders')
router.register('worker-orders', views.WorkerOrderViewSet, basename='worker-orders')
router.register('categories', views.CategoryViewSet, basename='categories')

app_name = 'order'
urlpatterns = [
    path('', include(router.urls))
]