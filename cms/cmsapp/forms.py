from django import forms
from .models import dModel, sModel

class dForm(forms.ModelForm):
	class Meta:
		model=dModel
		fields="__all__"


class sForm(forms.ModelForm):
	class Meta:
		model=sModel
		fields="__all__"