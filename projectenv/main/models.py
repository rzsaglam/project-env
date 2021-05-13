from django.db import models

# Create your models here.


class PaintList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Paint(models.Model):
    paintlist = models.ForeignKey(PaintList, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
