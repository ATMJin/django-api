from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def activate(self):
        self.is_active = True
        self.save()
