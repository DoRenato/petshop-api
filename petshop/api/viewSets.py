from rest_framework.viewsets import ModelViewSet
from petshop.models import Pet, Picture
from .serializers import PetSerializer, PictureSerializer
import os


class PetViewSet(ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    lookup_field = 'petId' # O recurso que a API irá buscar na url, sem esse campo o padrão é o id.


class PictureViewSet(ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    lookup_field = 'petId'

