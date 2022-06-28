from django.urls import include, path 
from rest_framework import routers 
from . import views 

router = routers.DefaultRouter()
router.register(r'login', views.LoginViewSet)
router.register(r'NewProd', views.NewProdViewSet)
router.register(r'Register', views.RegisterViewSet)

urlpatterns = [ 
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
namespace='rest_framework'))
]
