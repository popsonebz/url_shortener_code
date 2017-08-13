# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
import string
from django.db import models

# Create your models here.
def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))



class KirrURL(models.Model):
	url = models.CharField(max_length=220)
	shortcode = models.CharField(max_length=15, unique=True)
	updated = models.DateTimeField(auto_now=True) #everytime the model is saved
	timestamp = models.DateTimeField(auto_now_add=True) #when the model was created
	#empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False) #

	def __unicode__(self):
		return str(self.url)

	def save(self, *args, **kwargs): #overiding the default save
		self.shortcode = code_generator()
		super(KirrURL, self).save(*args, **kwargs)
