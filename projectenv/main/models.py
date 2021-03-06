from django.db import models

# Create your models here.


class Paint(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200, default="none")
    color = models.CharField(max_length=200)
    stock = models.IntegerField(default=0)
    KG20 = "20 KG"
    KG12 = "12 KG"
    KG5 = "5 KG"
    WEIGHTCHOISES = [
        (KG20, '20 KG'),
        (KG12, '12 KG'),
        (KG5, '5 KG'),
    ]
    weight = models.CharField(max_length=200, choices=WEIGHTCHOISES)
    IST = "İstanbul"
    YLV = "Yalova"
    LOCATIONCHOISES = [
        (IST, 'İstanbul'),
        (YLV, 'Yalova'),
    ]
    location = models.CharField(
        max_length=200, choices=LOCATIONCHOISES,)
    BOYA = "Boya"
    TINER = "Tiner"
    TYPECHOISES = [
        (BOYA, 'Boya'),
        (TINER, 'Tiner')
    ]
    choice = models.CharField(
        max_length=200, choices=TYPECHOISES,)

    def __str__(self):
        return self.name+' '+self.type+' '+self.color
