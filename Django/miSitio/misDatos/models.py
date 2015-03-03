from django.db import models

class MisDatos(models.Model):
	nombre = models.CharField(max_length=30)
	skills = models.TextField()
	telefono = models.IntegerField()
	email = models.EmailField()
	# nuevos campos 
	twitter = models.CharField(max_length=30)
	facebook = models.CharField(max_length=40)


	def __unicode__(self):
		return self.nombre