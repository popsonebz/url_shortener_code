# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .utils import code_generator, create_shortcode
from django.db import models

# Create your models here.



class KirrURL(models.Model):
	url = models.CharField(max_length=220)
	shortcode = models.CharField(max_length=15, unique=True, blank=True)
	updated = models.DateTimeField(auto_now=True) #everytime the model is saved
	timestamp = models.DateTimeField(auto_now_add=True) #when the model was created
	#empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False) #

	def __unicode__(self):
		return str(self.url)

	def save(self, *args, **kwargs): #overiding the default save
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode(self)
		super(KirrURL, self).save(*args, **kwargs)
