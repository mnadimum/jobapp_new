
from django import forms
from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        #fields = ['first_name', 'last_name', 'email']
        fields = '__all__'
        #exclude = ['last_name']
        help_texts = {
             'first_name': _('enter only characters'),
         }
        labels = {
            'first_name': _('Enter First Name'),
            'last_name': _('Enter Last Name'),
            'email': _("Enter your Email"),
            
        }
        


# def validate_comma(value):
#     if "," in value:
#         raise forms.ValidationError("Invalid ch entered")
#     return value


# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(max_length=100, label="Enter First Name")
#     last_name = forms.CharField(max_length=100, validators=[validate_comma], label="Enter Last Name")
#     email = forms.EmailField(max_length=100, label="Enter Email")
    
    # def clean_first_name(self):
    #     data = self.cleaned_data["first_name"]
    #     if "," in data:
    #         raise forms.ValidationError("Invalid First Name")
            
    #     return data
    
    
    
    
    
