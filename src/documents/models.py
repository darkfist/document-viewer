from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save


from .utils import unique_slug_generator

User = settings.AUTH_USER_MODEL

class Document(models.Model):
	uploaded_by	= models.ForeignKey(User)
	title 		= models.CharField(max_length=120, null=False, blank=False)
	description = models.TextField(null=True, blank=True)
	doc_url 	= models.FileField(null=True, blank=True)
	timestamp	= models.DateTimeField(auto_now_add=True)
	updated		= models.DateTimeField(auto_now=True)
	slug 		= models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.title

def document_pre_save_signal(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(document_pre_save_signal, sender=Document)