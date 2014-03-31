from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.translation import ugettext as _

class Home(models.Model):
	main_headline = models.CharField(max_length=200)
	main_snippet = models.TextField(max_length=1000)
	main_image = CloudinaryField('image')

	class Meta:
		verbose_name = _('Home')
		verbose_name_plural = _('Homes')

	def __unicode__(self):
		return 'Main headline'

	def save(self, *args, **kwargs):
		self.main_image.public_id = "{image}-{id}".format(image=self.main_headline, id=self.id)
		super(Home, self).save(*args, **kwargs)



class Service(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(max_length=1000)
	logo_image = CloudinaryField('image')

	class Meta:
		verbose_name = _('Service')
		verbose_name_plural = _('Services')

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.logo_image.public_id = "{image}-{id}".format(image=self.logo_image, id=self.id)
		super(Service, self).save(*args, **kwargs)



class About(models.Model):
	main_headline = models.CharField(max_length=200)
	description = models.TextField(max_length=2500)
	about_image = CloudinaryField('image')

	class Meta:
		verbose_name = _('About')
		verbose_name_plural = _('Abouts')

	def __unicode__(self):
		return 'About us'

	def save(self, *args, **kwargs):
		self.about_image.public_id = "{image}-{id}".format(image=self.main_headline, id=self.id)
		super(About, self).save(*args, **kwargs)

