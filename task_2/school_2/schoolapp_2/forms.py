from django import forms
from .models import Course, Request

class RequestForm(forms.ModelForm):
    MATERIAL_CHOICE = ((0, '-----'), (1, 'Paper'), (2, 'Pen'), (3, 'Text Book'), (4, 'Note Book'))
    materials = forms.MultipleChoiceField(choices=MATERIAL_CHOICE, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Request
        fields = ('rname', 'rdob', 'rdept','rcourse','gender','phone','email','address','purpose')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rcourse'].queryset = Course.objects.none()

        if 'rdept' in self.data:
            try:
                rdept_id = int(self.data.get('rdept'))
                self.fields['rcourse'].queryset = Course.objects.filter(deptid=rdept_id).order_by('cname')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['rcourse'].queryset = self.instance.rdept.course_set.order_by('cname')