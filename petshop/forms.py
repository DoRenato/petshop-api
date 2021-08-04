from django.forms import ModelForm
from .models import Pet, Picture


class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = ('__all__')


class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = ('picture',)
