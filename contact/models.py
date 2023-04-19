from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    subject = models.TextField(max_length=1500, null=False)

    def __str__(self):
        return self.name

