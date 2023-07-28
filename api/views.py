from rest_framework import viewsets

# Models
from users.models import User
from courses.models import Course
from reviews.models import Review
from complications.models import Complication
from directions.models import Direction
from professions.models import Profession

# Serializers
from .serializers import UserSerializer
from .serializers import CourseSerializer
from .serializers import ReviewSerializer
from .serializers import ComplicationSerializer
from .serializers import DirectionSerializer
from .serializers import ProfessionSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ComplicationViewSet(viewsets.ModelViewSet):
    queryset = Complication.objects.all()
    serializer_class = ComplicationSerializer


class DirectionViewSet(viewsets.ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
