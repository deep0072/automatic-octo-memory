from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null = True)
	phone  = models.CharField(max_length=200,  null = True)
	email = models.CharField(max_length=200, null = True)
	pic = models.ImageField(default= "5572575-SFICYMLP-6.jpg", null = True ,blank=True)
	date = models.DateTimeField(auto_now_add=True)
	


	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Product(models.Model):
	CATEGORY = (
		('Indoor', 'Indoor'),
		('Outdoor', 'Outdoor'),

		)
	name = models.CharField(max_length=200, null = True)

	price = models.FloatField(null = True)
	category = models.CharField(max_length=200, null = True, choices= CATEGORY)
	description = models.CharField(max_length=200, null = True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	tags = models.ManyToManyField(Tag)
	def __str__(self):
		return self.name


class Order(models.Model):
	STATUS = (
		('Pending', 'Pending'),
		('Out for delivery', 'Out for delivery'),
		('Delivered','Delivered' ),
		)
	Customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)

	Product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

	date_created = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=200, null = True , choices = STATUS)

	note = models.CharField(max_length=200, null = True)