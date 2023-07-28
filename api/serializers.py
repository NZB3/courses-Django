from rest_framework import serializers

# Models
from users.models import User
from courses.models import Course
from reviews.models import Review
from complications.models import Complication
from directions.models import Direction
from professions.models import Profession


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ComplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complication
        fields = '__all__'


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'
