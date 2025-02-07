from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)

class OtherModel(models.Model):
    related_model = models.ForeignKey(MyModel, on_delete=models.CASCADE)