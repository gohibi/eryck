from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
from users.forms import LoginForm , RegisterForm , Profileform
from django.http import HttpResponseRedirect

# Create your views here.

def log_in(request):
    context={}
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user:
                auth.login(request,user)
                messages.success(request, f'{username} , vous etes connectés')
                
                redirect_page  = request.POST.get("next",None)
                
                if redirect_page and redirect_page != reverse("users:logout"):
                    return HttpResponseRedirect(request.POST.get('next'))
                
                return HttpResponseRedirect(reverse('core:index'))
    else:
        form = LoginForm()
        
    context['title'] = "Authentification"
    context['Login'] = "Entrer"
    context['newaccount'] = "Créer un compte"
    context['forgotpassword'] ="Mot de passe oublié?"
    context['form'] = form
    return render(request,'users/login.html',context)


def register(request):
    context ={}
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request,user)
            messages.success(request,f"{user.username} vous etes inscrit avec succès & connectés à votre compte ")
            return HttpResponseRedirect(reverse('core:index'))
    else:
        form = RegisterForm()
    context['title'] = 'Inscription'
    context['register'] = "S'inscrire"
    context['form'] =form
    return render(request,'users/register.html',context)

@login_required
def profile(request):
    context={}
    if request.method == "POST":
        form_profile = Profileform(request.POST, instance=request.user , files=request.FILES)
        if form_profile.is_valid():
            form_profile.save()
            messages.success(request,"Mis à jour du profil effectué avec succès")
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form_profile = Profileform(instance=request.user)
    context['form'] = form_profile
    context['title'] = "Profil de l'utilisateur"
    context['header'] ="Mes annonces"
    return render(request,'users/profile.html',context)

def log_out(request):
    messages.warning(request,f"{request.user.username} , Vous etes deconnectés avec succes!")
    auth.logout(request)
    return redirect(reverse('core:index'))