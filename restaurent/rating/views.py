from rest_framework.viewsets import ModelViewSet
from .serializers import *


class RestaurentViewSet(ModelViewSet):
    queryset = Restaurent.objects.all()
    serializer_class = RestaurentSerializer

    
class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    
class StaffViewSet(ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    
class StaffSalaryViewSet(ModelViewSet):
    queryset = StaffSalary.objects.all()
    serializer_class = StaffSalarySerializer

    
class SalesViewSet(ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

    