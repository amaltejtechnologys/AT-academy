from django import forms
from .models import Enquiry, CallbackRequest, RecruiterContact


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'email', 'phone', 'course', 'branch', 'qualification']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'w-full px-4 py-2 border rounded-lg'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'w-full px-4 py-2 border rounded-lg'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter 10-digit mobile number', 'class': 'w-full px-4 py-2 border rounded-lg', 'maxlength': '10'}),
            'course': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
            'branch': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
            'qualification': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
        }

    def __init__(self, *args, pre_filled_course=None, pre_filled_branch=None, **kwargs):
        super().__init__(*args, **kwargs)
        if pre_filled_course:
            self.fields['course'].initial = pre_filled_course
            self.fields['course'].widget = forms.HiddenInput()
        if pre_filled_branch:
            self.fields['branch'].initial = pre_filled_branch
            self.fields['branch'].widget = forms.HiddenInput()


class CallbackForm(forms.ModelForm):
    class Meta:
        model = CallbackRequest
        fields = ['name', 'email', 'phone', 'course', 'branch']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'w-full px-4 py-2 border rounded-lg'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'w-full px-4 py-2 border rounded-lg'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter 10-digit mobile number', 'class': 'w-full px-4 py-2 border rounded-lg', 'maxlength': '10'}),
            'course': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
            'branch': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
        }

    def __init__(self, *args, pre_filled_course=None, pre_filled_branch=None, **kwargs):
        super().__init__(*args, **kwargs)
        if pre_filled_course:
            self.fields['course'].initial = pre_filled_course
            self.fields['course'].widget = forms.HiddenInput()
        if pre_filled_branch:
            self.fields['branch'].initial = pre_filled_branch
            self.fields['branch'].widget = forms.HiddenInput()


class RecruiterForm(forms.ModelForm):
    class Meta:
        model = RecruiterContact
        fields = ['name', 'email', 'phone', 'company_name', 'designation']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'w-full px-4 py-2 border rounded-lg'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'w-full px-4 py-2 border rounded-lg'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter 10-digit mobile number', 'class': 'w-full px-4 py-2 border rounded-lg', 'maxlength': '10'}),
            'company_name': forms.TextInput(attrs={'placeholder': 'Enter company name', 'class': 'w-full px-4 py-2 border rounded-lg'}),
            'designation': forms.TextInput(attrs={'placeholder': 'Your designation', 'class': 'w-full px-4 py-2 border rounded-lg'}),
        }
