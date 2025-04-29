from django.db import models
from datetime import datetime
from mpandraharaha.models import Tossaafiko
from userauths.models import User
from shortuuid.django_fields import ShortUUIDField 
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

    


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


class KaontyTvf(models.Model):
    isa = models.IntegerField() #Compte
    anarana = models.CharField(max_length=50, blank=True, null=True) #libellée
    rafitra = models.ForeignKey(Rafitra,related_name="kaonty_rafitra", null=True, on_delete=models.SET_NULL)
    
    class Meta:
        verbose_name_plural = "Kaontytvf" 
    
    def __str__(self):
        return f"{str(self.isa)} - {self.anarana}"

class KaontyTossaafiko(models.Model):
    tossaafiko = models.ForeignKey(Tossaafiko,null=True, related_name="kaonty_tossaafiko", on_delete=models.SET_NULL)
    kaontytvf = models.ForeignKey(KaontyTvf, related_name='kaontytvf', null=True, on_delete=models.SET_NULL)
    isa = models.IntegerField() #Compte
    anarana = models.CharField(max_length=50, blank=True, null=True) #libellée
    
    class Meta:
        verbose_name_plural = "KaontyTossaafiko" 
    
    def __str__(self):
        return f"{str(self.isa)} - {self.anarana}"


class Diarimbola(models.Model):
    taona = models.CharField(max_length=4, blank=True, null=True)
    tossaafiko = models.ForeignKey(Tossaafiko,null=True, related_name="diarimbola_tossaafiko", on_delete=models.SET_NULL)
    kaonty = models.ForeignKey(KaontyTossaafiko, null=True,blank=True, related_name="diarimbola_kaonty", on_delete=models.SET_NULL)
    vola_holaniana = models.IntegerField(default=0)
    vola_lany = models.IntegerField(default=0)
    vola_ambiny = models.IntegerField(default=0) 
    ecart = models.IntegerField(default=0)         
    fanamarihana = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Diarimbola" 
    
    def __str__(self):
        return f"{self.kaonty.isa} - {self.tossaafiko.anarana}"
    
class Laminasa(models.Model):
    taona = models.CharField(max_length=4, blank=True, null=True)
    tossaafiko = models.ForeignKey(Tossaafiko,null=True, related_name="laminasa_tossaafiko", on_delete=models.SET_NULL)
    diarimbola = models.ForeignKey(Diarimbola, null=True, related_name="laminasa_diarimbola", on_delete=models.SET_NULL)
    daty = models.DateField(default=datetime.now)
    asa = models.CharField(max_length=100, blank=True, null=True)
    # kaonty = models.ForeignKey(KaontyTossaafiko, related_name='laminasa_kaonty', null=True, blank=True, on_delete=models.SET_NULL)
    toerana = models.CharField(max_length=50, blank=True, null=True)
    fanamarihana = models.CharField(max_length=200, blank=True, null=True)
    tombana = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Laminasa" 
    
    def __str__(self):
        return f"{self.daty} {self.asa}"


class JournalCaisse(models.Model):
    taona = models.CharField(max_length=4, blank=True, null=True)
    tossaafiko = models.ForeignKey(Tossaafiko,null=True, related_name="journal_tossaafiko", on_delete=models.SET_NULL)
    diarimbola = models.ForeignKey(Diarimbola, null=True, related_name="journal_diarimbola", on_delete=models.SET_NULL)
    daty = models.DateField(default=datetime.now)
    miditra = models.IntegerField(default=0)
    mivoaka = models.IntegerField(default=0)
    ded = models.CharField(max_length=4, blank=True, null=True)
    pj_ded = models.ImageField(upload_to='pieces', null=True, blank=True)
    edr = models.CharField(max_length=4, blank=True, null=True)
    pj_edr = models.ImageField(upload_to='pieces', null=True, blank=True)
    solde = models.IntegerField(blank=True, null=True)
    fanamarihana = models.CharField(max_length=200, blank=True, null=True)
    

    class Meta:
        verbose_name_plural = "JournalCaisse" 
    
    def __str__(self):
        return f"{self.ded} {self.edr}"


""" Fonct: Pre and Post Save
    Diarimbola updated by Laminasa before and after save
    column: tombana 
"""
@receiver(post_save, sender=Laminasa)
def diarimbola_post_save(sender, instance, *args, **kwargs):
    laminasa = Laminasa.objects.filter(tossaafiko=instance.tossaafiko, diarimbola=instance.diarimbola.id)
     
    tombana=0  
    for l in laminasa:
        tombana += l.tombana
        
    if Laminasa:
        tombana = tombana
    else:
        tombana += instance.tombana
    
    Diarimbola.objects.filter(id=instance.diarimbola.id).update(vola_holaniana=tombana, vola_ambiny=tombana)

@receiver(pre_save, sender=JournalCaisse)
def diarimbola_journal_post_save(sender, instance, *args, **kwargs):
        pass
    
    
@receiver(post_save, sender=JournalCaisse)
def diarimbola_journal_post_save(sender, instance, *args, **kwargs):
    journalcaisse = JournalCaisse.objects.filter(tossaafiko=instance.tossaafiko, diarimbola=instance.diarimbola).order_by('-id')
    diarimbola = Diarimbola.objects.get(kaonty=instance.diarimbola.kaonty, tossaafiko=instance.diarimbola.tossaafiko)
    solde = 0
    vola_ambiny = 0
    vola_lany = 0
    
    if journalcaisse:
        for j in journalcaisse:
            print('solde init:', j.solde )
            if j.solde is not None or j.solde == 0:
                tossaafiko = j.tossaafiko.anarana
                solde = j.solde
                break

        if instance.fanamarihana == 'annulation':
            print('annulation')
            if instance.miditra != 0:
                solde += instance.miditra
                vola_ambiny = diarimbola.vola_ambiny + instance.miditra
                vola_lany = diarimbola.vola_lany
            if instance.mivoaka != 0:
                solde -= instance.mivoaka
                vola_lany = diarimbola.vola_lany
                vola_ambiny = diarimbola.vola_ambiny
                
        if instance.fanamarihana == 'reliquat':
            print('reliquat')
            if instance.mivoaka != 0:
                solde -= instance.mivoaka
                vola_lany = diarimbola.vola_lany
                vola_ambiny = diarimbola.vola_ambiny
               
                    
               
        else:
              if instance.miditra != 0:
                print('solde after =', solde)
                solde += instance.miditra
                vola_ambiny = diarimbola.vola_ambiny
                vola_lany = diarimbola.vola_lany
                print('Solde after after : ', solde, instance.miditra)
              if instance.mivoaka != 0:
                solde -= instance.mivoaka
                vola_lany = diarimbola.vola_lany + instance.mivoaka 
              if diarimbola.vola_ambiny == 0:
                vola_ambiny = diarimbola.vola_holaniana - instance.mivoaka
              else:    
                vola_ambiny = diarimbola.vola_ambiny - instance.mivoaka
        if vola_lany != 0 or diarimbola.vola_holaniana != 0:
            ecart = (vola_lany / diarimbola.vola_holaniana) * 100
        else:
            ecart = 0   
        JournalCaisse.objects.filter(id=instance.id).update(solde=solde) 
        Diarimbola.objects.filter(id=instance.diarimbola.id).update(vola_lany=vola_lany, vola_ambiny=vola_ambiny, ecart=ecart)
        
    
   
    



################################ ATTENTE EVOLUTION ########################################################


# class Ded(models.Model):
#     mpitantsorabola = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='mpitantsorabola', verbose_name='Mpitantsoratry ny vola')
#     tossaafiko = models.ForeignKey(Tossaafiko, null=True, related_name="ded_tossaafiko", on_delete=models.SET_NULL)
    
#     num_ded =  models.CharField(max_length=3, verbose_name='DED')
#     daty_ded =  models.DateField(default=datetime.now, verbose_name='Daty nanaovana DED')
    
#     laminasa = models.ForeignKey(Laminasa,null=True, related_name="diarimbola_laminasa", on_delete=models.SET_NULL )
#     diarimbola = models.ForeignKey(Diarimbola,null=True, related_name="ded_diarimbola", on_delete=models.SET_NULL)
#     fandaniana = models.IntegerField()
#     sata = models.CharField(max_length=10, choices=SATA, default='en_cours')
    
#     class Meta:
#         verbose_name_plural = "Ded" 
    
#     def __str__(self):
#         return f"{self.tossaafiko} - {self.num_ded} - {self.diarimbola}"
    
# class Fanamarinana_ded(models.Model):
#     ded = models.ForeignKey(Ded, null=True, on_delete=models.SET_NULL)
#     mpanamarina_birao_ssa = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='mpanamarina_toby_ssa')
#     mpanamarina_toby = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='mpanamarina_toby')
#     mpanamarina_birao_tvf = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='mpanamarina_birao_tvf')
    
    
    
    

    
