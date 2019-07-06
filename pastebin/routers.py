from pastes.api.viewsets import PasteViewSet, UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pastes', PasteViewSet)
router.register('users', UserViewSet)
