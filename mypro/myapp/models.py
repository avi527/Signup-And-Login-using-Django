from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
#start one to one relation
class Customer(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        related_name='vehicle'
        )
    def __str__(self):
        return self.name
class Teacher(models.Model):
	name=models.CharField(max_length=50)
	mobilenumber=models.CharField(max_length=10)
	def __str__(self):
		return self.name

class Student(models.Model):
	studentname=models.CharField(max_length=30)
	clastime=models.TimeField() 
	subject=models.CharField(max_length=20)
	Teacher=models.OneToOneField(Teacher,on_delete=models.CASCADE,related_name='Student')
	def __str__(self):
		return self.studentname
#end one to one relation

#start one to many relation
class Laptop(models.Model):
	brand=models.CharField(max_length=20)
	generation=models.CharField(max_length=10)
	def __str__(self):
		return self.brand
class Language(models.Model):
	name=models.CharField(max_length=10)
	uses=models.CharField(max_length=20)
	Laptop=models.ForeignKey(Laptop,on_delete=models.CASCADE,related_name='Language')
	def __str__(self):
		return self.name
#end one to many relation

#start many to many relation
class Worker(models.Model):
	name=models.CharField(max_length=20)
	working_area=models.CharField(max_length=15)
	def __str__(self):
		return self.name
class Machine(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ManyToManyField(
        Worker,
        related_name='Machine'
    )
    def __str__(self):
    	return self.name

#end many to many relation
class Cus(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)

# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()

