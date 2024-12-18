from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from .models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorSerializer, SensorInfoSerializer


class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor
    serializer_class = SensorSerializer

class MeasurementsView(CreateAPIView):
    queryset = Measurement
    serializer_class = MeasurementSerializer    

class ListSensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor
    serializer_class = SensorInfoSerializer
    

       

