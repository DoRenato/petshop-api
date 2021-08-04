from django.shortcuts import render, redirect
from .models import *
from .services import get_pets
from .forms import PetForm

# Create your views here.

def pet(request):
    form = PetForm(request.POST or None)
    pet = get_pets() # função onde busca os pets na api, arquivo services.py
    if request.method == 'POST':
        form.save()
        return redirect('pet')
    else:
        return render(request, 'petshop/pet.html', {'pet':pet, 'form':form})


def edit_pet(request, petId):
    pet = Pet.objects.get(petId=petId)
    form = PetForm(request.POST or None, instance=pet)
    if request.method == 'POST':
        form.save()
        return redirect('pet')
    else:
        return render(request, 'petshop/edit_pet.html', {'pet':pet, 'form':form})

def delete_pet(request, petId):
    pet = Pet.objects.get(petId=petId)
    pet.delete()
    return redirect('pet')
    