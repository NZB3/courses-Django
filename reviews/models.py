from django.db import models
from users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    assessment = models.IntegerField(default=1, validators=[
                                                    MaxValueValidator(5),
                                                    MinValueValidator(1)
                                                ])
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review')

    def str(self):
        return self.title

    def get_absolute_url(self):
        return f'/review/{self.id}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['-title', ]