from django.db import models
from shortuuid.django_fields import ShortUUIDField #pip shortuuid django package
from django.utils.html import mark_safe
from userauths.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import RegexValidator


TOSSAAFIKO = (
    ("stk", "STK"),
    ("ssa", "SSA"),
    ("fdl", "FDL"),
    ("toby_fifaliana", "Toby Fifaliana"),
    ("toby_fitiavana", "Toby Fitiavana"),
    ("toby_fahamarinana", "Toby Fahamarinana"),
    ("toby_fiadanana", "Toby Fiadanana"),
)

ANDRAIKITRA = (
    ("filoha", "Filoha"),
    ("filoha_mpanampy", "Filoha Mpanampy"),
    ("tonia", "Mpitan-tsoratry ny fivoriana"),
    ("tonia_vola", "Mpitan-tsoratry ny vola"),
    ("mpitahiry_vola", "Mpitahiry Vola"),
    ("mpanolo_tsaina", "Mpanolo-tsaina"),
    ("mpiakambana", "Mpikambana"),
    ("mpitarika_rantsana", "Mpitarika Rantsana"),
    ("mpianatra_ssa", "Mpianatra SSA"),
    ("mpampianatra_ssa", "Mpampianatra SSA"),
)

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Ankohonana(models.Model):
    ankid = ShortUUIDField(unique=True, length=10, max_length=30, prefix="pad", alphabet="abcdefgh12345")
    anarana = models.CharField(max_length=50, blank=True, null=True)
    faritra = models.CharField(max_length=8, blank=True, null=True)
    
    
    class Meta:
        verbose_name_plural = "Ankohonana" 
        
    def __str__(self):
        return self.anarana


class Tossaafiko(models.Model):
    said = ShortUUIDField(unique=True, length=10, max_length=30, prefix="said", alphabet="abcdefgh12345")
    anarana = models.CharField(verbose_name='tossaafiko',choices=TOSSAAFIKO, max_length=17, default="ssa")
    # mpiangona = models.ManyToManyField(Mpiangona, related_name='mpiangona', null=True)    
    fanamarihana = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Tossaafiko" 
        
    def __str__(self):
        return f"{self.anarana}" 


class Mpiangona(models.Model):
    piid = ShortUUIDField(unique=True, length=10, max_length=30, prefix="pgn", alphabet="abcdefgh12345")
    
    name = models.CharField(max_length=100, verbose_name="Anarana")
    surname = models.CharField(max_length=100, verbose_name="Fanampin'anarana")
    
    toerana = models.CharField(max_length=100,default="Zanaka", help_text="Toerana misy azy eo anivon'ny ankohonana")
    # tossaafiko = models.ManyToManyField(Tossaafiko, related_name='tossaafiko', null=True, blank=True)
    
    
    image = models.ImageField(upload_to="mpiangona", default=('i8.jpg'), verbose_name="Sary")
    # description  = models.TextField(null=True, blank=True, default="I am an Amazing Vendor")
    description  = models.CharField(max_length=500, null=True, blank=True, default="Mpiangona ato FJKM Tranovato Faravohitra", verbose_name="Fanamarihana",help_text="Filazana ny mombamomba ny mpiangona")
    # description  = RichTextUploadingField(null=True, blank=True, default="Mpiangona ato FJKM Tranovato Faravohitra", verbose_name="Fanamarihana",help_text="Filazana ny mombamomba ny mpiangona")
    address = models.CharField(max_length=100, default="Antananarivo", verbose_name="Adiresy")
    contact = models.CharField(max_length=13,validators=[RegexValidator(r'^\d\d\d \d\d \d\d\d \d\d' , message="Tsy atao abd fa tarehimarika ary asiana elanelany")], help_text="034 10 466 70", verbose_name="Finday")  
    
    ankohonana = models.ForeignKey(Ankohonana, related_name="ankohonana", on_delete=models.SET_NULL, null=True, help_text="Mitondra ny anaran'ny Ray lohan'ny fianakaviana")  
    
    
    zanaka = models.IntegerField(default=0, verbose_name="Zanaka", help_text="Isan'ny zanaka")
    class Meta:
        verbose_name_plural = "Mpiangona" 
    

    def mpiangona_image(self):
        return mark_safe('<img src="%s" width="50 height="50 />' % (self.image.url))
    
    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Mpikambana(models.Model):
    pikid = ShortUUIDField(unique=True, length=10, max_length=30, prefix="pikid", alphabet="abcdefgh12345")
    mpiangona = models.ForeignKey(Mpiangona, on_delete=models.SET_NULL, null=True)
    tossaafiko = models.ForeignKey(Tossaafiko, related_name='tossaafiko', on_delete=models.SET_NULL, null=True)
    andraikitra = models.CharField(max_length=18,choices=ANDRAIKITRA)
    
    class Meta:
        verbose_name_plural = "Mpikambana" 
        
    def __str__(self):
        return f"{self.mpiangona.name} {self.mpiangona.surname}"

class Mpandray(models.Model):
    paid = ShortUUIDField(unique=True, length=10, max_length=30, prefix="pad", alphabet="abcdefgh12345")
    mpandray_mpiangona = models.ForeignKey(Mpiangona, related_name="mpandray_mpiangona", on_delete=models.SET_NULL, null=True, verbose_name='Mpiangona')
    karatra = models.CharField(max_length=6,validators=[RegexValidator(r'^[V|L]-\d\d\d\d', message="Atao mitovy amin'ny ohatra io ambany io azafady") ],help_text="V-0000 na L-0000" ,blank=True, null=True)
    taona = models.DateField()
    fiangonana = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "Mpandray" 
        
    def __str__(self):
        return self.karatra
    


   
