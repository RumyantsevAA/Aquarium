from app1.models import *
from django import forms

'''
class NewAquarium(forms.Form):
	name = forms.CharField(label='Название', max_length=100)
	volume = forms.IntegerField(label='Объём')
'''

class NewAquarium(forms.ModelForm):
	class Meta:
		model=Aquarium
		fields = ["Volume", "Name"]

class EditAquarium(forms.Form):
	name = forms.CharField(label='Название', max_length=100)
	volume = forms.IntegerField(label='Объём')

class NewFish(forms.Form):
#	OPTIONS = (("a", "A"),("b", "B"),)
	fishTypeList = forms.ModelChoiceField(queryset=FishType.objects.all(), empty_label=None, widget=forms.Select(attrs={'style': 'width:200px', 'size':'20'}))
	count = forms.IntegerField(label='Количество')
	answer = forms.BooleanField(label="Yes?")

class LoginForm(forms.Form):
	username = forms.CharField(label='Логин', max_length=100)
	password = forms.CharField(label='Пароль', max_length=100)

class RegisterForm(forms.Form):
	username = forms.CharField(label='Логин', max_length=100)
	password = forms.CharField(label='Пароль', max_length=100)