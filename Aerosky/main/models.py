from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    phone = models.CharField(max_length=64, blank=True)
    subject = models.CharField(max_length=128)
    message = models.TextField(max_length=4096)

    def __str__(self):
        return f"Name: {self.name} | Subject: {self.subject}"
