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


class ItemComment(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name="comments",  # item.comments.all()
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
