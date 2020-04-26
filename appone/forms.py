from django import forms

class Form_Input(forms.Form):
	def __init__(self,*args,**kwargs):

		self.temp = kwargs.pop('text')
		super().__init__(*args,**kwargs)
		self.fields['code_input'].initial=self.temp
		
		

	temp = "Enter Your Code Here.."
	lang = [ ('PYTHON','Python'),('C','C'),('CPP','C++'),('JAVA','Java')]
	code_input = forms.CharField(widget = forms.Textarea(attrs={'placeholder': temp,'cols':120,'rows':15}),label="")
	temp = "Custom input"
	custom_input = forms.CharField(widget = forms.Textarea(attrs={'placeholder': temp,'cols':120,'rows':5}),label="",required=False)
	language= forms.CharField(label='', widget=forms.Select(choices=lang))
	action = forms.CharField(label='', widget=forms.HiddenInput())

class Form_Output(forms.Form):
	def __init__(self,*args,**kwargs):
		
		self.temp = kwargs.pop('text')
		super().__init__(*args,**kwargs)
		self.fields['code_output'].initial=self.temp

	temp = "Output Is Shown Here.."
	code_output = forms.CharField(widget = forms.Textarea(attrs={'placeholder': temp,'cols':120,'rows':5}),label="")