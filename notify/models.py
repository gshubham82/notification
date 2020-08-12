from django.db import models

# Create your models here.
STATUS_CHOICE = (
    ("1","High"),
    ("2", "Medium"),
    ("3", "Low"),
    ("4", "Very Low"),
)
class Notification(models.Model):
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(max_length=1000)
    status = models.CharField(max_length=1, default='1', choices=STATUS_CHOICE)

    class Meta:
        ordering = ['status']

    def __str__(self):
        return f"{self.date}, {self.time}, {self.message}, {self.status}"
