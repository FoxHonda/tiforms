from django.db import models
from django.urls import reverse

class Post(models.Model):
	text = models.CharField(max_length=30)
	post_date = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ['post_date',]


	def get_absolute_url(self):
		return reverse('post-detail', args=[str(self.id)])

class PostImages(models.Model):
	image = models.ImageField(blank=True)
	order = models.IntegerField(default=0)
	post = models.ForeignKey('Post', on_delete=models.CASCADE)

	class Meta:
		ordering = ['order',]