from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Rocker(models.Model):

	user = models.ForeignKey(User)
	about = models.TextField()

	def __unicode__(self):
		return self.user.username