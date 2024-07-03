from django.urls import path
from services.views import annonces,result,delete_annoce,update_annonce


app_name = "services"

urlpatterns = [
    path('annonces/vendre-des-kg/',annonces,name="annonces"),
    path('annonces/resultat/', result,name="resultat"),
    path('annonce/delete/<int:id>',delete_annoce,name="delete"),
    path('annonce/modifier/<int:id>',update_annonce,name="update")
]