from django.db import models


class ExampleModel(models.Model):
    example_object = models.CharField(max_length=250)

    def __str__(self):
        return self.example_object
