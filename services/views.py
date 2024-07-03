from django.shortcuts import render , redirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from services.forms import TravelForm,AnnonceForm
from services.models import Annonce,Travel
from django.template.loader import render_to_string
# Create your views here.
@login_required
def annonces(request):
    context={}
    if request.method == "POST":
        formT = TravelForm(request.POST,request.FILES)
        formA =  AnnonceForm(request.POST)
        
        if formT.is_valid() and formA.is_valid():
            travel = formT.save()
            annonce = formA.save(commit=False)
            annonce.travel = travel
            annonce.user = request.user
            annonce.status = "disponible"
            annonce.save()
            messages.success(request, "Annonce ajouté avec succès")
            
            redirect_page  = request.POST.get("next",None)
            if redirect_page and redirect_page != reverse("users:logout"):
                return HttpResponseRedirect(request.POST.get('next'))
            
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        formT = TravelForm()
        formA = AnnonceForm()
        
    context['form_annonce'] = formA
    context['form_travel'] = formT
    return render(request,'services/annonce.html',context)
    
    
# class Resultat(View):
#     def get(self, request):
#         items = Annonce.objects.all().order_by('-id')
#         return render(request,'services/result.html',{'items':items})

def result(request):
    items = Annonce.objects.all().order_by('-id')
    return render(request,'core/index.html',{'items':items})


def delete_annoce(request,id):
    annonce = Annonce.objects.get(pk=id)
    annonce.delete()
    return HttpResponseRedirect(reverse('users:profile'))


def update_annonce(request,id):
    return render(request,'services/modifier-annonce.html')