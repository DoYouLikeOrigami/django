from django.db import models
from django.utils import timezone
# tpublish = models.DateTimeField('Дата публикации', default=timezone.now)

# Create your models here.
class Driver(models.Model):
	passport = models.CharField('Паспорт', max_length=20)
	driverclass = models.CharField('Класс', max_length=20)
	experience = models.CharField('Опыт', max_length=20)
	status = models.CharField('Статус', max_length=20)
	payment = models.IntegerField('Зарплата')

	class Meta:
		verbose_name = 'Водитель'
		verbose_name_plural = 'Водители'
			
	def __str__(self):
		return self.passport