from django.urls import path,include
from student.api import views
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('user',views.userviewset,basename='user')
router.register('application',views.applicationviewset,basename='application')

urlpatterns = [
    path('',include(router.urls))
]

