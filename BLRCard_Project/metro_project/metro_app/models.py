from django.db import models

class Journey(models.Model):
    datetime = models.DateTimeField()
    from_zone = models.IntegerField()
    to_zone = models.IntegerField()