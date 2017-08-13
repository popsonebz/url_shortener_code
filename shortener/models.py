# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class KirrURL(models.Model):
	url = models.CharField(max_length=220)

	def __unicode__(self):
		return str(self.url)
