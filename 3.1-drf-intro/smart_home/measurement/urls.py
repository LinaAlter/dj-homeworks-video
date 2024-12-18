from django.urls import path
from django.contrib import admin
from .views import ListSensorsView, SensorView, SensorDetailView, MeasurementsView


urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('admin/', admin.site.urls),
    path('sensors/', ListSensorsView.as_view()),
    path('sensors/<int:pk>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementsView.as_view())
]
