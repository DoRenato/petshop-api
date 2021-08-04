from rest_framework.viewsets import ModelViewSet
from petshop.models import Pet, Picture
from .serializers import PetSerializer, PictureSerializer


class PetViewSet(ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PictureViewSet(ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

