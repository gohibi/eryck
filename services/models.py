from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.text import slugify
from users.models import User
from django.utils.html import mark_safe

# Create your models here.
typevoyage = (
    ('Aller simple','Aller Simple'),
    ('Aller retour','Aller-Retour')
)
status = (
    ('disponible','Disponible'),
    ('vendu','Vendu'),
)



class Travel(models.Model):
    type = models.CharField(choices=typevoyage,max_length=50 ,verbose_name="Type de voyage")
    slug =models.SlugField(max_length=100,unique=True,blank=True,null=True)
    file = models.ImageField(upload_to="Flight tickets/",blank=True, null=True,verbose_name="Capture billet d'avion " )
    airline = models.CharField(max_length=200 ,blank=False, null=False , verbose_name="COmpagnie aerienne")
    flight_number = models.CharField(max_length=15,blank=False, null=False)
    origin = models.CharField(max_length=100 , blank=False, null=False)
    destination = models.CharField(max_length=100 , blank=False, null=False)
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    
    class Meta:
        verbose_name_plural = "Travels"
        ordering = ['-id']
    
    def __str__(self):
        return f'{self.airline}-{self.flight_number}'
    
    def image_plane_ticket(self):
        if self.file:
            return mark_safe(f'<img src="{self.file.url}" width="50" height="50">')
        return 'No plane ticket image'
    
    def save(self,*args,**kwargs):
        if not self.slug:
            value =f'{self.airline}-{self.flight_number}'
            self.slug =slugify(value,allow_unicode=True)
        return super().save(*args,**kwargs)
    
    
class Annonce(models.Model):
    aid = ShortUUIDField(length=8, max_length=15 , prefix="ANN", alphabet="0123456789")
    user = models.ForeignKey(to=User , on_delete=models.CASCADE , verbose_name="annonceur")
    travel = models.ForeignKey(to=Travel, on_delete=models.CASCADE,verbose_name="voyage" , related_name="travel")
    title = models.CharField(max_length=150 , verbose_name="Nom de l'annonce")
    description = models.TextField(blank=False,null=False , verbose_name="Description de l'annonce")
    capacity = models.PositiveIntegerField(blank=False, null=False , verbose_name="Capacité restante")
    price = models.DecimalField(max_digits=10,decimal_places=0,verbose_name="Prix par kilo")
    date_publication = models.DateTimeField(auto_now_add=True , verbose_name="Date de publication")
    slug = models.SlugField(max_length=100,unique=True,blank=True, null=True)
    status = models.CharField(choices=status,max_length=30)
    
    class Meta:
        verbose_name_plural = "Annonces"
        ordering = ["-id"]
    
    def save(self,*args,**kwargs):
        if not self.slug:
            value = f'{self.aid}'
            self.slug =slugify(value,allow_unicode=True)
        return super().save(*args,**kwargs)

    def get_total(self):
        return round(self.price * self.capacity,0)
    
    def days_left(self):
       if self.travel.departure_date and self.date_publication:
           return (self.travel.departure_date - self.date_publication).days
       return None
   
    def __str__(self):
        return f"Annonce de {self.user} du {self.date_publication} pour le vol {self.travel}"