from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from .models import Driver
from .forms import DriverForm

# Create your views here.

def driversCreate(request):
	if request.method == 'POST':
		form = DriverForm(request.POST)

		if form.is_valid():
			passport = form.cleaned_data['passport']
			driverclass = form.cleaned_data['driverclass']
			experience = form.cleaned_data['experience']
			status = form.cleaned_data['status']
			payment = form.cleaned_data['payment']

			driver = Driver(passport=passport, driverclass=driverclass, experience=experience, status=status, payment=payment)
			driver.save()

			return HttpResponseRedirect('/drivers/list/')

		else:
			return HttpResponseRedirect('/drivers/create/')

	else:
		form = DriverForm()
		content = {
			'Title' : 'Добавление водителя',
			'Form' : form,
			'Action' : 'create/',
			'ButtonText' : 'Добавить'}

		return render(request, "form.jinja2", content)



def driversDelete(request, id=None):
	DriverInfo = get_object_or_404(Driver, id=id)
	DriverInfo.delete()
	return HttpResponseRedirect('/drivers/list/')



def driversDetail(request, id=None):
	DriverInfo = get_object_or_404(Driver, id=id)
	content = {
		'Title' : DriverInfo.passport,
		'DriverInfo' : DriverInfo
	}
	return render(request, "index.jinja2", content)



def driversList(request):
	querylist = Driver.objects.all
	content = {
		'Title' : 'Список',
		'Drivers' : querylist
	}
	return render(request, "index.jinja2", content)



def driversUpdate(request, id=None):
	DriverInfo = get_object_or_404(Driver, id=id)

	if request.method == 'POST':
		form = DriverForm(request.POST)

		if form.is_valid():
			DriverInfo.passport = form.cleaned_data['passport']
			DriverInfo.driverclass = form.cleaned_data['driverclass']
			DriverInfo.experience = form.cleaned_data['experience']
			DriverInfo.status = form.cleaned_data['status']
			DriverInfo.payment = form.cleaned_data['payment']

			DriverInfo.save()

			return HttpResponseRedirect('/drivers/detail/' + str(DriverInfo.id) + '/')

		else:
			return HttpResponseRedirect('/drivers/update/' + str(DriverInfo.id) + '/')

	else:
		form = DriverForm()
		action = 'update/' + str(DriverInfo.id) + '/'
		content = {
			'Title' : 'Изменение водителя',
			'Form' : form,
			'DriverInfo' : DriverInfo,
			'Action' : action,
			'ButtonText' : 'Изменить'}

		return render(request, "form.jinja2", content)
