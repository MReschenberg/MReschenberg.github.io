from django.db import models

# Create your models here.
class Post(models.Model):
	body = models.TextField()

	class Admin:
		pass