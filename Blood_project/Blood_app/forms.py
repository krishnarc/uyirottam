from django import forms
from Blood_app.models import Add_donors

class Add_donors_form(forms.ModelForm):
    class Meta():
        model = Add_donors
        fields = '__all__'
