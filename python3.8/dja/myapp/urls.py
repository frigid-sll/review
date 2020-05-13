from rest_framework.routers import DefaultRouter
from myapp import views

router = DefaultRouter()
router.register('',views.HelloWorldViewSet,base_name="hello")

urlpatterns = router.urls