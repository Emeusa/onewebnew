from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import AoneEducational, Account

class AeducationalForm(ModelForm):
    
    class Meta:
        model = AoneEducational
        fields = ['profile_code', 'last_name', 'first_name', 'middle_name', 'date_of_birth', 'gender', 'genotype', 'b_group', 'marital', 'madien_name', 'email', 'contact_add', 'nin', 'mobile_number', 'nationality', 'state_of_origin', 'local_gov', 'parent_name', 'occupation', 'office_add', 'phone_no', 'parent_mail', 'alevel_pro', 'prefered_ex_state', 'exam_town', 'first_choices', 'programme_one', 'second_choices', 'programme_two', 'utme_sub_one', 'utme_sub_two', 'utme_sub_three', 'utme_sub_four', 'name_of_sec', 'exam_type', 'reg_mode', 'yr_of_exam', 'serial_no', 'pin_no', 'exam_no', 'num_of_sit', 'olevel_sub_one', 'grade1', 'olevel_sub_two', 'grade2', 'olevel_sub_three', 'grade3', 'olevel_sub_four', 'grade4', 'olevel_sub_five', 'grade5', 'olevel_sub_six', 'grade6', 'olevel_sub_sev', 'grade7', 'olevel_sub_eig', 'grade8', 'olevel_sub_nin', 'grade9']

        widgets = {
            'profile_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'For JAMB Candidates'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Surname'}),
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'middle_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Middle Name'}),
            'date_of_birth': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Date of Birth', 'type':'date'}),
            'gender': forms.Select(attrs={'class':'form-control', 'placeholder':'gender'}),
            'genotype': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Genotype'}),
            'b_group': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blood Group'}),
            'marital': forms.Select(attrs={'class':'form-control', 'placeholder':'Marital Satus'}),
            'madien_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Madien Name(if married)'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your Email'}),
            'contact_add': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Contact Address'}),
            'nin': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your NIN'}),
            'mobile_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Phone No.'}),
            'nationality': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Nationality'}),
            'state_of_origin': forms.Select(attrs={'class':'form-control', 'placeholder':'Your State'}),
            'local_gov': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your L.G.A'}),
            'parent_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Parent Name'}),
            'occupation': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Occupation'}),
            'office_add': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Office Address'}),
            'phone_no': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone No.'}),
            'parent_mail': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'alevel_pro': forms.Select(attrs={'class':'form-control'}),
            'prefered_ex_state': forms.Select(attrs={'class':'form-control'}),
            'exam_town': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Exam Town'}),
            'first_choices': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Choice'}),
            'programme_one': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Programme of Study'}),
            'second_choices': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Second Choice'}),
            'programme_two': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Programme of Study'}),
            'utme_sub_one': forms.Select(attrs={'class':'form-control'}),
            'utme_sub_two': forms.Select(attrs={'class':'form-control'}),
            'utme_sub_three': forms.Select(attrs={'class':'form-control'}),
            'utme_sub_four': forms.Select(attrs={'class':'form-control'}),
            'name_of_sec': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of Secondary Sch.'}),
            'exam_type': forms.Select(attrs={'class':'form-control'}),
            'reg_mode': forms.Select(attrs={'class':'form-control'}),
            'yr_of_exam': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Exams Year'}),
            'serial_no': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Serial No.'}),
            'pin_no': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Pin No.'}),
            'exam_no': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Exam No.'}),
            'num_of_sit': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Number of Sitting'}),
            'olevel_sub_one': forms.Select(attrs={'class':'form-control'}),
            'grade1': forms.Select(attrs={'class':'form-control'}),
            'olevel_sub_two': forms.Select(attrs={'class':'form-control'}),
            'grade2': forms.Select(attrs={'class':'form-control'}),
            'olevel_sub_three': forms.Select(attrs={'class':'form-control'}),
            'grade3': forms.Select(attrs={'class':'form-control'}),
            'olevel_sub_four': forms.Select(attrs={'class':'form-control'}),
            'grade4': forms.Select(attrs={'class':'form-control'}),
            'olevel_sub_five': forms.Select(attrs={'class':'form-control'}),
            'grade5': forms.Select(attrs={'class':'form-control'}),
            'olevel_sub_six': forms.Select(attrs={'class':'form-control'}),
            'grade6': forms.Select(attrs={'class':'form-control'}),
            'olevel_sub_sev': forms.Select(attrs={'class':'form-control'}),
            'grade7': forms.Select(attrs={'class':'form-control'}),
            'olevel_sub_eig': forms.Select(attrs={'class':'form-control'}),
            'grade8': forms.Select(attrs={'class':'form-control'}),
            'olevel_sub_nin': forms.Select(attrs={'class':'form-control'}),
            'grade9': forms.Select(attrs={'class':'form-control'}),
        }




class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text="Required. Add an email address.")

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.get(email=email)

        except Exception as e:
            return email

        raise forms.ValidationError(f"Email {email} is already in use.")


    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.get(username=username)

        except Exception as e:
            return username

        raise forms.ValidationError(f"Username {username} is already in use.")
