from home.views import AboutViewSet,CampusRecuitmentViewSet,AcknowledgementViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('About',AboutViewSet)
router.register('CampusRecuitment',CampusRecuitmentViewSet)
router.register('Acknowledgement',AcknowledgementViewSet)

