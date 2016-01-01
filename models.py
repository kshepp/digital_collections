from django.db import models

from autoslug import AutoSlugField
from django.core.files import File

class Collection(models.Model):
    title = models.TextField()
    location = models.SlugField()
    cover_image = models.FileField(blank=True)
    # python manage.py migrate
    # python manage.py makemigrations


    def __unicode__(self):
		return self.title

class Item(models.Model):

	def __unicode__(self):
		return self.title

	# image = models.ImageField()
	title = models.TextField()
	location = AutoSlugField(populate_from='title',editable=True,unique=True)
	creator = models.TextField(blank=True)
	publisher = models.TextField(blank=True)
	date = models.TextField(blank=True)
	file_format = models.TextField(blank=True)
	subject = models.TextField(blank=True)
	description = models.TextField(blank=True)
	language = models.TextField(blank=True)
	source = models.TextField(blank=True)
	rights = models.TextField(blank=True)
	resolution = models.CharField(max_length=100,blank=True)
	quality = models.TextField(blank=True)
	notes = models.TextField(blank=True)
	file_up = models.FileField(blank=True)
	collections = models.ManyToManyField(Collection,blank=True)


class Exhibit(models.Model):
    
    def __unicode__(self):
		return self.title

    layout_choices = (
    	(0,"Text"),
    	(1,"Text and Image"),
    	(2,"Gallery"),
    	(3,"Map"),
    )
    title = models.TextField()
    exhibit_image = models.FileField(blank=True)
    location = AutoSlugField(populate_from='title',editable=True,unique=True)
    text = models.TextField(blank=True)
    layout = models.IntegerField(choices=layout_choices, default=0)
    items = models.ManyToManyField(Item,blank=True)





