from django.db import models


class Direction(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, unique=True, null=True)
    description = models.TextField()

    def str(self):
        return self.title

    def get_absolute_url(self):
        return f'/directions/{self.id}'

    class Meta:
        verbose_name = 'Direction'
        verbose_name_plural = 'Directions'
        ordering = ['-title', ]
