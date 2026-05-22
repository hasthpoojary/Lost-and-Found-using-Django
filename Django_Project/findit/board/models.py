from django.db import models

class Item(models.Model):
    ITEM_TYPE = [
        ('lost', 'Lost'),
        ('found', 'Found'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    item_type = models.CharField(max_length=10, choices=ITEM_TYPE)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title