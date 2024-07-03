from django.urls import path
from users.views import log_in,register,log_out,profile

app_name = "users"

urlpatterns = [
    path('connexion/',log_in,name="login"),
    path('inscription/',register,name="register"),
    path('deconnexion/',log_out,name="logout"),
    path('profil/',profile, name="profile"),
    
]