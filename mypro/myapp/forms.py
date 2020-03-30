# from django.froms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.model import User
from django import forms  
from myapp.models import Profile  

# from .model import Order,Profile

# class OrderForm(ModelForm):
# 	class Meta:
# 		model = Order
# 		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

