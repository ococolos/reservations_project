from django.db import models


class City(models.Model):
    class Meta:
        verbose_name_plural = "Cities"

    city_name = models.CharField(max_length=25)
    city_commision = models.FloatField()

    def __str__(self):
        return self.city_name


class Reservations(models.Model):
    class Meta:
        verbose_name_plural = "Reservations"
        
    property_name = models.CharField(max_length=40)
    city = models.CharField(max_length=25)
    net_income = models.FloatField()
    date = models.DateField(null=True)

    def __str__(self):
        return self.property_name
