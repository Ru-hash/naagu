from django import forms
from .models import Dress

class DressForm(forms.ModelForm):
	class Meta:
		model =Dress
		fields = [
		'name' ,
		'price' ,
		'quantity',
		'image',
		'description' ,
		'variety',
		]

class DressUpdateForm(forms.ModelForm):
	class Meta:
		model = Dress
		fields = [

		'price' ,
		'quantity',
		'image',
		
		]