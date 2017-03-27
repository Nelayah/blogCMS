import os
from django.db import models
from django.utils.deconstruct import deconstructible
from uuid import uuid4

@deconstructible
class PathAndRename(object):
	def __init__(self, sub_path):
		self.path = sub_path

	def __call__(self, instance, filename):
		ext = filename.split('.')[-1]
		# set filename as random string
		filename = '{}.{}'.format(uuid4().hex, ext)
		# return the whole path to the file
		return os.path.join(self.path, filename)

def RenameImage():
	path_and_rename = PathAndRename("avatars/")
	return path_and_rename

class Gallery(models.Model):
	title = models.CharField(max_length=100)
	images = models.ImageField(upload_to=RenameImage(), null=True, blank=True)
	time = models.DateField(db_index=True, auto_now_add=True)

	def __str__(self):
		return self.title

	class Meta:
		db_table = "gallery"