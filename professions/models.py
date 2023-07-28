from django.db import models
from directions.models import Direction


class Profession(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=True)
    description = models.TextField()
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='professions', null=True)

    def str(self):
        return self.title

    def get_absolute_url(self):
        return f'/professions/{self.id}'

    class Meta:
        verbose_name = 'Profession'
        verbose_name_plural = 'Professions'
        ordering = ['-title', ]
