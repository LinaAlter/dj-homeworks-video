from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=80)



class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)

