from django.db import models

class Title(models.Model):
    title = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
