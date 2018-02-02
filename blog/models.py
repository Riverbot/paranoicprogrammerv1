from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.

class UrlFormatField(models.CharField):
  def to_python(self, value):
    return value.replace(" ","_").lower()

class Category(models.Model):
	author = models.ForeignKey('auth.User', on_delete = models.PROTECT)
	parent_category = models.ForeignKey("self", default = None, blank=True, null=True, on_delete = models.PROTECT)
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Subject(models.Model):
	author = models.ForeignKey('auth.User', on_delete = models.PROTECT)
	category = models.ForeignKey("Category", default = None, on_delete = models.PROTECT)
	name = models.CharField(max_length=200)
	url_name =  UrlFormatField(max_length=200)
	thumb_image = models.ImageField(default = None, blank=True, null=True)
	
	def __str__(self):
		return self.name

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete = models.PROTECT)
	title = models.CharField(max_length=200)
	text = RichTextField()
	date_created = models.DateTimeField(default = timezone.now)
	date_published = models.DateTimeField(blank = True, null = True)
	subject = models.ForeignKey("Subject", default = None, on_delete = models.PROTECT)

	def __str__(self):
		return self.title
