from django.db import models

class ContactUsDetails(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name

class Registration(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    dob = models.DateField()
    experience = models.TextField()

    def __str__(self):
        return self.name

class Donation(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    pin_code = models.CharField(max_length=10)
    purpose = models.CharField(max_length=255)

    def __str__(self):
        return self.name
