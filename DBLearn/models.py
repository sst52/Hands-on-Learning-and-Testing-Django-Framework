from django.db import models

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=4) # Now we cannot enter more than 4 characters inside the character field....
	description = models.TextField()
	price = models.DecimalField(max_digits=10000,decimal_places=2)
	summary = models.TextField(default='this is cool')
	