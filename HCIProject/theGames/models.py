from django.db import models

# Create your models here.

class Event(models.Model):
	name = models.CharField(max_length=128, unique=True)

	def __unicode__(self):
		return self.name

class specificEvent(models.Model):
	event = models.ForeignKey(Event)
	title = models.CharField(max_length=128)
	url = models.URLField()
	
	def __unicode__(self):
		return self.title