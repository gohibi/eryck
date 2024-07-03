from django.contrib import admin
from .models import Travel, Annonce

# Register your models here.
@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    list_display = ['type','image_plane_ticket','airline','flight_number','origin','destination','departure_date','arrival_date']
    
    
    
class AnnonceAdmin(admin.ModelAdmin):
    list_display = ['user','travel','title','description','capacity','price','date_publication']
    
    
admin.site.register(Annonce,AnnonceAdmin)
