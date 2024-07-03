from services.models import Annonce

def get_annonces(request):
    if request.user.is_authenticated:
        return Annonce.objects.filter(user=request.user)