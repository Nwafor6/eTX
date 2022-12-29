from  django import forms
from mainapp.models import AdmittedSession,Semester,Student,SessionCompleted,Course


class AddSessionForm(forms.ModelForm):
	session_title=forms.CharField(widget= forms.TextInput(attrs={"placeholder":"2018/2019","class":"form-control", "id":"exampleInputUsername1"}),required=True, max_length = 100, label="Session Title",help_text="'2018/2019'")
	class Meta:
		model=AdmittedSession
		fields=['session_title']