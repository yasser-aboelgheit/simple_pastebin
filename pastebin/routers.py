from pastes.api.viewsets import PasteViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pastes',PasteViewSet)