from django.db import models
from shortuuid.django_fields import ShortUUIDField #pip shortuuid django package
from django.utils.html import mark_safe
from userauths.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)