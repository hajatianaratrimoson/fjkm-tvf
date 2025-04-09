from django.db import models
from shortuuid.django_fields import ShortUUIDField #pip shortuuid django package
from django.utils.html import mark_safe
from userauths.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import RegexValidator
from datetime import datetime

SATA = (
    ("mianatra", "Mianatra"),
    ("mpandray", "Mpandray"),
)
TOSSAAFIKO = (
    ("stk", "STK"),
    ("ktt", "KTT"),
    ("ssa", "SSA"),
    ("fdl", "FDL"),
    ("aam", "AAM"),
    ("safif", "SAFIF"),
    ("fafi", "FAFI"),
    ("fmo", "FMO"),
    ("svm", "SVM"),
    ("dorkasy", "DORKASY"),
    ("vfl", "VFL"),
    ("zr", "ZR"),
    ("sampati", "SAMPATI"),
    ("amboarampeo", "AMBOARAMPEO"),
    ("aff", "AFF"),
    ("kpsv", "KPSV"),
    ("kga", "KGA"),
    ("kff", "KFF"),
    ("kvo", "KVO"),
    ("kftl", "KFTL"),
    ("kmb", "KMB"),
    ("tpram", "TPRAM"),
    ("toby_fifaliana", "TOBY FIFALIANA"),
    ("toby_fitiavana", "TOBY FITIAVANA"),
    ("toby_fahamarinana", "TOBY FAHAMARINANA"),
    ("toby_fiadanana", "TOBY FIADANANA"),
)

ANDRAIKITRA = (
    ("filoha", "Filoha"),
    ("filoha_mpanampy", "Filoha Mpanampy"),
    ("tonia", "Mpitan-tsoratry ny fivoriana"),
    ("tonia_vola", "Mpitan-tsoratry ny vola"),
    ("mpitahiry_vola", "Mpitahiry Vola"),
    ("mpanolo_tsaina", "Mpanolo-tsaina"),
    ("mpikambana", "Mpikambana"),
    ("mpitarika_rantsana", "Mpitarika Rantsana"),
    ("mpianatra_ssa", "Mpianatra SSA"),
    ("mpampianatra_ssa", "Mpampianatra SSA"),
    ("coach_rantsana", "Coaach Rantsana"),
    ("mpitarika_sampati", "Mpitarika Sampati"),
)

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Ankohonana(models.Model):
    # ankid = ShortUUIDField(unique=True, length=10, max_length=30, prefix="pad", alphabet="abcdefgh12345")
   
    anarana = models.CharField(max_length=50, blank=True, null=True, help_text="Anaran'ny raim-pianakaviana")
    fokotany = models.CharField(max_length=50, blank=True, null=True, help_text="Anaran'ny raim-pianakaviana")
    faritra = models.CharField(max_length=8, blank=True, null=True, help_text="faritra misy ny toerana hipetrahan'ny ankohonana")
    faritra_tvf = models.CharField(max_length=8, blank=True, null=True, help_text="faritra misy ny toerana hipetrahan'ny ankohonana nofaritan'ny TVF")
    firenena = models.CharField(max_length=8, blank=True, null=True, help_text="Firenena misy azy ankehitriny")
    
    
    
    class Meta:
        verbose_name_plural = "Ankohonana" 
        
    def __str__(self):
        return self.anarana


class Tossaafiko(models.Model):
    # said = ShortUUIDField(unique=True, length=10, max_length=30, prefix="said", alphabet="abcdefgh12345")
    
    anarana = models.CharField(verbose_name='tossaafiko',choices=TOSSAAFIKO,unique=True,  max_length=17, default="ssa", help_text="Anarana oentin'ny Tossaafiko", error_messages= {'required': 'Efa misy io anarana io'})   
    fanamarihana = models.TextField(blank=True, null=True, help_text="Ny mombamomba ny Tossaafiko")
    
    class Meta:
        verbose_name_plural = "Tossaafiko" 
        
    def __str__(self):
        return f"{self.anarana}" 


class Mpiangona(models.Model):
    # piid = ShortUUIDField(unique=True, length=10, max_length=30, prefix="pgn", alphabet="abcdefgh12345")
    
    anarana = models.CharField(max_length=30, verbose_name="Anarana")
    anarana_zatovo = models.CharField(max_length=30, verbose_name="Anarana zatovo", null=True, blank=True)
    fanampiny = models.CharField(max_length=25, verbose_name="Fanampin'anarana")
    toerana = models.CharField(max_length=100,default="Zanaka", help_text="Toerana misy azy eo anivon'ny ankohonana")
    sary = models.ImageField(upload_to="mpiangona", default=('i8.jpg'), verbose_name="Sary")
    daty_nahaterahana = models.DateField(verbose_name='Daty nahaterahana', blank=True, null=True)
    fanamarihana  = models.CharField(max_length=500, null=True, blank=True, default="Mpiangona ato FJKM Tranovato Faravohitra", verbose_name="Fanamarihana",help_text="Filazana ny mombamomba ny mpiangona")
    
    # description  = RichTextUploadingField(null=True, blank=True, default="Mpiangona ato FJKM Tranovato Faravohitra", verbose_name="Fanamarihana",help_text="Filazana ny mombamomba ny mpiangona")
    
    adiresy = models.CharField(max_length=100, default="Antananarivo", verbose_name="Adiresy")
    finday = models.CharField(max_length=13,validators=[RegexValidator(r'^\d\d\d \d\d \d\d\d \d\d' , message="Tsy atao abd fa tarehimarika ary asiana elanelany")], help_text="034 10 466 70", verbose_name="Finday")  
    finday_2 = models.CharField(max_length=13,validators=[RegexValidator(r'^\d\d\d \d\d \d\d\d \d\d' , message="Tsy atao abd fa tarehimarika ary asiana elanelany")], help_text="034 10 466 70", verbose_name="Finday hafa", null=True, blank=True)  
    mailaka = models.EmailField(null=True, blank=True, verbose_name="Mailaka")
    
    ankohonana = models.ForeignKey(Ankohonana, related_name="ankohonana", on_delete=models.SET_NULL, null=True, help_text="Mitondra ny anaran'ny Ray lohan'ny fianakaviana")  
    zanaka = models.IntegerField(default=0, verbose_name="Zanaka", help_text="Isan'ny zanaka")
    
    asa = models.CharField(max_length=50, verbose_name="Asa", null=True, blank=True)
    fanomezana = models.CharField(max_length=50, verbose_name="Fanomezam-pahasoavana", null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Mpiangona" 
    

    def mpiangona_image(self):
        return mark_safe('<img src="%s" width="50 height="50 />' % (self.image.url))
    
    def __str__(self):
        return f"{self.anarana} {self.fanampiny}"
    
class Mpikambana(models.Model):
    # pikid = ShortUUIDField(unique=True, length=10, max_length=30, prefix="pikid", alphabet="abcdefgh12345")
    
    mpikambana = models.ForeignKey(Mpiangona, related_name='mpikambana', on_delete=models.SET_NULL, null=True)
    tossaafiko = models.ForeignKey(Tossaafiko, related_name='tossaafiko', on_delete=models.SET_NULL, null=True)
    andraikitra = models.CharField(max_length=18,choices=ANDRAIKITRA, help_text="Andraikitra ao amin'ny Tossaafiko")
    
    class Meta:
        verbose_name_plural = "Mpikambana" 
        
    def __str__(self):
        return f"{self.mpikambana}"

class Mpandray(models.Model):
    # paid = ShortUUIDField(unique=True, length=10, max_length=30, prefix="pad", alphabet="abcdefgh12345")
    
    mpandray = models.ForeignKey(Mpiangona, related_name="mpandray_mpiangona", on_delete=models.SET_NULL, null=True, verbose_name='Mpandray')
    
    karatra = models.CharField(max_length=6,validators=[RegexValidator(r'^[V|L]-\d\d\d\d', message="Atao mitovy amin'ny ohatra io ambany io azafady") ],help_text="V-0000 na L-0000" ,blank=True, null=True)
    taona = models.DateField(help_text='Taona naha mpandray')
    fiangonana = models.CharField(max_length=50, help_text='Fiangonana nanamasinana ho mpandray')
    
    class Meta:
        verbose_name_plural = "Mpandray" 
        
    def __str__(self):
        return self.karatra
    

class Batisa(models.Model):
    anarana = models.ForeignKey(Mpiangona, related_name="batisa_mpiangona", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Anarana" )
    
    daty_nanolorana = models.DateField(verbose_name="Daty nanolorana", default=datetime.now, null=True, blank=True)
    daty_batisa = models.DateField(verbose_name="Daty batisa", default=datetime.now, null=True, blank=True)
    rad = models.ManyToManyField(Mpiangona, verbose_name="Ray aman-dReny", null=True, blank=True)
    fiangonana = models.CharField(max_length=50, help_text="Fiangonana nanaovana batisa", null=True, blank=True)
    firenena = models.CharField(max_length=25, help_text="Firenena nanaovana batisa", null=True, blank=True)
    class Meta:
        verbose_name_plural = "Batisa"
    
    def __str__(self):
        return f"{self.anarana}"


class Katekomena(models.Model):
    anarana = models.ForeignKey(Mpiangona, related_name="katekomena_mpiangona", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Anarana" )
    
    andiany =  models.CharField(max_length=20, help_text="Anarana oentin'ny andian'ny katekomena", null=True, blank=True)
    daty_nidirana = models.DateField(verbose_name="Daty nidirana nianatra", default=datetime.now, null=True, blank=True)
    daty_nivoahana = models.DateField(verbose_name="Daty nivoahana katekomena", default=datetime.now, null=True, blank=True)
    fiangonana = models.CharField(max_length=50, help_text="Fiangonana namoahana azy", null=True, blank=True)
    firenena = models.CharField(max_length=25, help_text="Firenena namoahana azy", null=True, blank=True)
    sata = models.CharField(max_length=15, choices=SATA, default='mianatra') 
    class Meta:
        verbose_name_plural = "Katekomena"
    
    def __str__(self):
        return f"{self.anarana}"
   
