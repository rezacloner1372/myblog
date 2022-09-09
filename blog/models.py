from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime
# Create your models here.


def validate_file_extention(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extentions = ['.jpg', '.png', '.jpeg']
    if not ext.lower() in valid_extentions:
        raise ValidationError('Unsupported file extension.')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(
        upload_to='files/user_avatar', null=False, blank=False, validators=[validate_file_extention])
    description = models.CharField(max_length=512, null=False, blank=False)


class Article(models.Model):
    title = models.CharField(max_length=512, null=False, blank=False)
    cover = models.FileField(
        upload_to='files/article_cover/', null=False, blank=False, validators=[validate_file_extention])
    content = RichTextField()
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)
    cover = models.FileField(
        upload_to='files/category_cover/', null=False, blank=False, validators=[validate_file_extention])
