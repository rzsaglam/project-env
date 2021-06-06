from django.db import models

# Create your models here.


class Paint(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200, default="none")
    color = models.CharField(max_length=200)
    stock = models.IntegerField(default=0)
    IST = "İstanbul"
    YLV = "Yalova"
    LOCATIONCHOISES = [
        (IST, 'İstanbul'),
        (YLV, 'Yalova'),
    ]
    location = models.CharField(
        max_length=200, choices=LOCATIONCHOISES, default=IST)

    def __str__(self):
        return self.name+' '+self.type+' '+self.color
