from django.conf.urls import url
from rest_framework import routers
from api.views import LinkViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'links', LinkViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls
