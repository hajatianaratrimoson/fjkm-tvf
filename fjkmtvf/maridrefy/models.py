from django.db import models

# from django.conf import settings
# from django.contrib.sites.models import Site
# from django.contrib.redirects.models import Redirect

from datetime import datetime
from mpandraharaha.models import Tossaafiko
from userauths.models import User
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import pre_save
from django.dispatch import receiver
import inspect
from django.db import IntegrityError
from sqlite3 import IntegrityError
from django.http import HttpResponse

# from django.contrib.sites.models import Site
# from django.contrib.redirects.models import Redirect

def get_current_user():
        for frame_record in inspect.stack():
            if frame_record[3] == 'get_response':
                request = frame_record[0].f_locals['request']
                break
            else:
                request = None
        return request.user.id
    
class Sondage(models.Model):
    anonymous = models.IntegerField(null=False, blank=False, default=get_current_user)
    sigara = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Sondage" 
    
    def __str__(self):
        return str(self.anonymous)


@receiver(pre_save, sender=Sondage)
def my_handler(sender, instance, *args, **kwargs):
    current_user = get_current_user()
    sondage = Sondage.objects.filter(anonymous=current_user)
    print('sondage = ', sondage)
    if sondage is None:
        print('sondage is None')
        instance.anonymous = current_user
    else:
        pass
    #    Redirect.objects.create(
    #                 site_id=Site.objects.get_current().id,
    #                 old_path=f"/admin/maridrefy/sondage/",
    #                 new_path=f"/admin/maridrefy/sondage/",
    #             )
    
   
        
   


