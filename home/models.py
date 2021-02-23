
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 300)
    email = models.CharField(max_length = 300)
    subject = models.CharField(max_length = 300)
    message = models.TextField()

    def __str__(self):
        return self.name

class Contactinformation(models.Model):
    address = models.CharField(max_length = 300)
    tole = models.CharField(max_length = 300)
    contact_no = models.CharField(max_length = 300)
    time = models.CharField(max_length = 300)
    email = models.CharField(max_length = 300)

    def __str__(self):
        return self.address
class testimonial(models.Model):
    name = models.CharField(max_length = 300)
    post = models.CharField(max_length = 300)
    comment = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.name