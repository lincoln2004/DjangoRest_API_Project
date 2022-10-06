from rest_framework import viewsets, authentication as auth, permissions as perm

from .Serializers import FruitSerializer, VegetalSerializer

from .models import fruits, vegetals



class fruitViewSet(viewsets.ModelViewSet):
    
    queryset = fruits.objects.all()
    
    serializer_class = FruitSerializer
    
    authentication_classes = [ auth.BasicAuthentication, ]
    
    permission_classes = [ perm.DjangoModelPermissions, ]
    

class vegetalViewSet(viewsets.ModelViewSet):
    
    queryset = vegetals.objects.all()
    
    serializer_class = VegetalSerializer
    
    authentication_classes = [ auth.BasicAuthentication, ]
    
    permission_classes = [ perm.DjangoModelPermissions, ]
    
        