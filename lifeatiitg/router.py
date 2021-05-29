from lifeatiitg.views import ContentsViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('Content',ContentsViewSet)