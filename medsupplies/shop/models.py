from django.db import models

# Create your models here.
from django.db import models

class PageContent(models.Model):
    PAGE_CHOICES = [
        ('home', 'Home'),
        ('about', 'About'),
        ('services', 'Services'),
        ('staff', 'Staff'),
        ('equipments', 'Equipments'),
        ('testimonials', 'Testimonials'),
        ('contact', 'Contact'),
    ]

    page_name = models.CharField(max_length=50, choices=PAGE_CHOICES, unique=True)
    title = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True)

    def __str__(self):
        return f"{self.get_page_name_display()} Page"

