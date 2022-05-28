from django.db import models

class dModel(models.Model):
	did=models.IntegerField(primary_key=True)
	dname=models.CharField(max_length=20)

	def __str__(self):
		return self.dname


class sModel(models.Model):
	rno=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=20)
	dept = models.ForeignKey(dModel, on_delete=models.CASCADE )

	def __str__(self):
		return self.name