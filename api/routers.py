from rest_framework import routers
from .views import UserViewSet, CourseViewSet, ReviewViewSet, \
                   ComplicationViewSet, DirectionViewSet, ProfessionViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'complications', ComplicationViewSet)
router.register(r'directions', DirectionViewSet)
router.register(r'professions', ProfessionViewSet)
