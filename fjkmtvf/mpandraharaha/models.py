from django.db import models
from shortuuid.django_fields import ShortUUIDField #pip shortuuid django package
from django.utils.html import mark_safe
from userauths.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Mpiangona(models.Model):
    vid = ShortUUIDField(unique=True, length=10, max_length=30, prefix="pgn", alphabet="abcdefgh12345")
    
    name = models.CharField(max_length=100, default="vaovao")
    surname = models.CharField(max_length=100, default="vaovao")
    
    image = models.ImageField(upload_to="mpiangona", default=('i8.jpg'))
    #description  = models.TextField(null=True, blank=True, default="I am an Amazing Vendor")
    description  = RichTextUploadingField(null=True, blank=True, default="I am an Amazing Vendor")
    address = models.CharField(max_length=100, default="Antananarivo")
    contact = models.CharField(max_length=100, default="+261 (34) 99 999 999")    
    
    class Meta:
        verbose_name_plural = "Mpiangona" 
    

    def mpiangona_image(self):
        return mark_safe('<img src="%s" width="50 height="50 />' % (self.image.url))
    
    def __str__(self):
        return self.surname