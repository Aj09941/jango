from django.db import models

# Create your models here.
class Services(models.Model):
	"""docstring for Services"""
	title = models.CharField(max_length=200)
	description = models.TextField()
	
	def __str__(self):
		return self.title


class FeatureImages(models.Model):
	"""docstring for FeatureImages"""
	title = models.CharField(max_length=100, blank=True, null=True)
	image = models.ImageField(upload_to='images/')

class FeatureImagesTwo(models.Model):

	image = models.ImageField(upload_to='images/')

class Events(models.Model):
	"""docstring for Events"""
	title = models.CharField(max_length=200)
	description = models.TextField()
	start_date = models.DateField(auto_now=True)
	end_date = models.DateField(auto_now=True)

	def __str__(self):
		return self.title