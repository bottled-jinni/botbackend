from __future__ import unicode_literals

from django.db import models

class Node(models.Model):
	#Add foreing key to bot type
	name     = models.CharField(max_length=256, null=False, blank=True)
	infected = models.BooleanField(blank=True, default=False)
	url 	 = models.CharField(max_length=256, null=True, blank=True)  
	rank	 = models.IntegerField(null=True, blank=True)