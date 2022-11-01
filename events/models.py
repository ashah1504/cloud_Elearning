from django.db import models

# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=400)
    time = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
 
    class Meta:
        verbose_name_plural = 'Events'
