from django.db import models

# Create your models here.
class Product():
	title = models.TextField()
	description = models.TextField()
	price = models.TextFiled()
	