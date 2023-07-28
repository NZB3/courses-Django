from django.db import models

from users.models import User
from reviews.models import Review
from professions.models import Profession
from complications.models import Complication


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=True)
    description = models.TextField()
    video = models.FileField(blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_course')
    review = models.ManyToManyField(Review, related_name='course')
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, related_name='course')
    complication = models.ForeignKey(Complication, on_delete=models.CASCADE, related_name='course')

    def str(self):
        return self.title

    def get_absolute_url(self):
        return f'/course/{self.id}'

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['-title', ]
