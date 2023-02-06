from django import forms
from .models import Req,Dep,Course

class ReqForm(forms.ModelForm):

    material=forms.MultipleChoiceField(choices=Req.MATERIAL_CHOICE,widget=forms.CheckboxSelectMultiple,required=False)
    class Meta:
        model=Req
        fields=['name','dob','gender','phone','email','address','department','course','purpose']
