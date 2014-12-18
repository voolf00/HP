from  django.forms import ModelForm
from medic.models import Profile, PotientList


class Patient_list_Form(ModelForm):
    class Meta():
        model = PotientList
        fields = {'diagnoz','vypiska','obj_3d'}


class User_form_datails(ModelForm):
    class Meta():
        model = Profile
        fields = ['first_name', 'second_name', 'last_name', 'is_who']

