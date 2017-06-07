from django import forms

class DriverForm(forms.Form):
	passport = forms.CharField(label='Паспорт', max_length=20)
	driverclass = forms.CharField(label='Класс', max_length=20)
	experience = forms.CharField(label='Опыт', max_length=20)
	status = forms.CharField(label='Статус', max_length=20)
	payment = forms.IntegerField(label='Зарплата')