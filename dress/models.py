from django.db import models
from django.urls import reverse
from PIL import Image
# Create your models here.
class Dress(models.Model):
	name = models.CharField(max_length=30)
	price = models.IntegerField()
	variety = models.CharField(max_length=30,null=True,blank=True)
	description = models.TextField(null=True,blank=True)
	quantity = models.IntegerField(default=1)
	image = models.ImageField(default='default.jpg', upload_to='dress_pic')
	def get_absolute_url(self):
		return reverse('dress:detail', kwargs={'pk': self.pk})
	def save(self, *args, **kwargs):
		super().save(*args,**kwargs)
		img = Image.open(self.image.path)

		if img.height > 500 or img.width > 500:
			output_size = (500, 500)
			img.thumbnail(output_size)
			img.save(self.image.path)
