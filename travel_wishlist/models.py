from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

# This will create a Database with name, visited, date_visited and note fields.
class Place(models.Model):
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    date_visited = models.DateTimeField(blank=True, null=True)
    comment = models.TextField()


    def __str__(self):
        return '%s visited? %s ' %(self.name, self.visited)
