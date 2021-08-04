from rest_framework.serializers import ModelSerializer
from petshop.models import Pet, Picture


class PetSerializer(ModelSerializer):
    class Meta:
        model = Pet
        fields = ('__all__')


class PictureSerializer(ModelSerializer):
    class Meta:
        model = Picture
        fields = ('__all__')