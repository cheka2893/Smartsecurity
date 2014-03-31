from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.translation import ugettext as _

class Gallery_Image(models.Model):
	image_slide = CloudinaryField('image')
	slug = models.SlugField(max_length=300, unique=True)

	class Meta:
		verbose_name = _('Gallery_Image')
		verbose_name_plural = _('Gallery_Images')

	def __unicode__(self):
		return "Galery {id}".format(id=self.id)

	def save(self, *args, **kwargs):
		self.slug = 'image_slide_{id}'.format(id=self.id)
		self.image_slide.public_id = "image_slide-{id}".format(id=self.id)
		super(Gallery_Image, self).save(*args, **kwargs)

    