#adds bits from other files:
from django.db import models
from django.utils import timezone

class Post(models.Model):							#defines model as an object
	author = models.ForeignKey('auth.User')			#link to another model
	title = models.CharField(max_length=200)		#defines text with lim. characters
	text = models.TextField()						#long text without limit
	created_date = models.DateTimeField(			#date and time
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title