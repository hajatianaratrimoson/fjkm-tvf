from django.db import models
from datetime import datetime
from mpandraharaha.models import Tossaafiko
from userauths.models import User
from shortuuid.django_fields import ShortUUIDField 

AXE = (
    ("asa_fitoriana_filazantsara", "Asa Fitoriana Filazantsara"),
    ("asa_fanabeazana", "Asa Fanabeazana"),
    ("asa_sosialy", "Asa Sosialy"),
    ("asa_iombonana", "Asa Iombonana"),  
)

SATA = (
    ("en_cours", "En cours"),
    ("valide", "Validé"),  
)

# Cadre Logique
class Rafitra(models.Model):
    axe = models.CharField(max_length=30, choices=AXE)
    fanamarihana = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Rafitra" 
    
    def __str__(self):
        return self.axe

class Kaonty(models.Model):
    isa = models.IntegerField() #Compte
    anarana = models.CharField(max_length=50, blank=True, null=True) #libellée
    rafitra = models.ForeignKey(Rafitra,related_name="kaonty_rafitra", null=True, on_delete=models.SET_NULL)
    
    class Meta:
        verbose_name_plural = "Kaonty" 
    
    def __str__(self):
        return f"{str(self.isa)} - {self.anarana}"
    
class Laminasa(models.Model):
    tossaafiko = models.ForeignKey(Tossaafiko,null=True, related_name="laminasa_tossaafiko", on_delete=models.SET_NULL)
    daty = models.DateField(default=datetime.now)
    asa = models.CharField(max_length=100, blank=True, null=True)
    toerana = models.CharField(max_length=50, blank=True, null=True)
    fanamarihana = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Laminasa" 
    
    def __str__(self):
        return f"{self.daty} {self.asa}"

class Diarimbola(models.Model):
    kaonty = models.ForeignKey(Kaonty, null=True, related_name="diarimbola_kaonty", on_delete=models.SET_NULL)
    vola = models.IntegerField()        
    fanamarihana = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Diarimbola" 
    
    def __str__(self):
        return f"{self.kaonty.isa} - {self.vola}"


class Ded(models.Model):
    mpitantsorabola = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='mpitantsorabola', verbose_name='Mpitantsoratry ny vola')
    tossaafiko = models.ForeignKey(Tossaafiko, null=True, related_name="ded_tossaafiko", on_delete=models.SET_NULL)
    
    num_ded =  models.CharField(max_length=3, verbose_name='DED')
    daty_ded =  models.DateField(default=datetime.now, verbose_name='Daty nanaovana DED')
    
    laminasa = models.ForeignKey(Laminasa,null=True, related_name="diarimbola_laminasa", on_delete=models.SET_NULL )
    diarimbola = models.ForeignKey(Diarimbola,null=True, related_name="ded_diarimbola", on_delete=models.SET_NULL)
    fandaniana = models.IntegerField()
    sata = models.CharField(max_length=10, choices=SATA, default='en_cours')
    
    class Meta:
        verbose_name_plural = "Ded" 
    
    def __str__(self):
        return f"{self.daty_ded} - {self.num_ded}"
    
class Fanamarinana_ded(models.Model):
    ded = models.ForeignKey(Ded, null=True, on_delete=models.SET_NULL)
    mpanamarina_birao_ssa = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='mpanamarina_toby_ssa')
    mpanamarina_toby = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='mpanamarina_toby')
    mpanamarina_birao_tvf = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='mpanamarina_birao_tvf')
    
    
    
    

    
