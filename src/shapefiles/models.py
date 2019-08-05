from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models as gis_models

# Create your models here.

class Parcel(models.Model):
	objectid = models.BigIntegerField()
	parcelkey 	= models.CharField(max_length=26)
	ownerid 	= models.CharField(max_length=30)
	registered	= models.CharField(max_length=50)
	eastparcel	= models.CharField(max_length=50)
	westparcel	= models.CharField(max_length=50)
	northparce	= models.CharField(max_length=50)
	southparce	= models.CharField(max_length=50)
	parcelnoen	= models.BigIntegerField()
	shape_area	= models.FloatField()
	geom		= gis_models.MultiPolygonField(srid=4326)

	def __unicode__(self):
		return self.parcelkey

class Building(models.Model):
	objectid = models.BigIntegerField()
	houseno = models.CharField(max_length=15)
	parcelkey = models.CharField(max_length=30)
	shape_leng = models.FloatField()
	area = models.FloatField()
	geom = gis_models.MultiPolygonField(srid=4326)

	def __unicode__(self):
		return self.parcelkey

class Transportation(models.Model):
	objectid = models.BigIntegerField()
	name = models.CharField(max_length=50)
	shape_leng = models.FloatField()
	shape_area = models.FloatField()	
	geom = gis_models.MultiPolygonField(srid=4326)
	
	def __unicode__(self):
		return self.name

class Hydro(models.Model):
	objectid = models.BigIntegerField()
	name = models.CharField(max_length=50)
	shape_leng = models.FloatField()
	shape_area = models.FloatField()
	hydrotype = models.BigIntegerField()
	geom = gis_models.MultiPolygonField(srid=4326)
	
	def __unicode__(self):
		return self.name
