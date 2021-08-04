from django.shortcuts import render, redirect
from .models import *
from .services import *
from .forms import PetForm

# Create your views here.

def pet(request):
    pet = get_pets() # função onde busca os pets na api, arquivo services.py
    # pictures = get_pictures()
    if request.method == 'POST':
        novopet={}
        novopet['petId'] = request.POST['petId']
        novopet['nome_pet'] = request.POST['nome']
        novopet['dono'] = request.POST['dono']
        novopet['raca'] = request.POST['raca']
        novopet['nascimento'] = request.POST['nasc']
        post_pet(novopet)
        return redirect('pet')
    else:
        return render(request, 'petshop/pet.html', {'pet':pet})


def edit_pet(request, petId):
    pet = Pet.objects.get(petId=petId)
    if request.method == 'POST':
        editpet={}
        editpet['petId'] = request.POST['petId']
        editpet['nome_pet'] = request.POST['nome']
        editpet['dono'] = request.POST['dono']
        editpet['raca'] = request.POST['raca']
        editpet['nascimento'] = request.POST['nasc']
        put_pet(editpet, petId)
        return redirect('pet')
    else:
        return render(request, 'petshop/edit_pet.html', {'pet':pet})


def delete_pet(request, petId):
    del_pet(petId)
    return redirect('pet')

# def edit_pet(request, petId):
#     pet = Pet.objects.get(petId=petId)
#     form = PetForm(request.POST or None, instance=pet)
#     if request.method == 'POST':
#         form.save()
#         return redirect('pet')
#     else:
#         return render(request, 'petshop/edit_pet.html', {'pet':pet, 'form':form})

# def delete_pet(request, petId):
#     pet = Pet.objects.get(petId=petId)
#     pet.delete()
#     return redirect('pet')
    