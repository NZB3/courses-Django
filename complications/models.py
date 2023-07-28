from django.db import models


class Complication(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=True)
    description = models.TextField()

    def str(self):
        return self.title

    def get_absolute_url(self):
        return f'/complications/{self.id}'

    class Meta:
        verbose_name = 'Complication'
        verbose_name_plural = 'Complications'
        ordering = ['-title', ]
