from django.db import models

class Title(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.title