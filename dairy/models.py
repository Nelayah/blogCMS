from django.db import models
from django.contrib.postgres.fields import ArrayField

class Dairy(models.Model):
	title = models.CharField(max_length=100, unique=True)
	tag = ArrayField(models.CharField(max_length=100), blank=True)
	slug = models.SlugField(max_length=60, unique=True)
	digest = models.CharField(max_length=200, null=True, blank=True)
	content = models.TextField()
	time = models.DateField(db_index=True, auto_now_add=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('time',)
		db_table = "dairy"