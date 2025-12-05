from django import forms
from _global.dc_forms import *

from .models import Contact, ContactInformation

class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "description"]
        
    name = dc_form_fields_char(label="Name", help_text="The name of the contact", placeholder="Tung Tung Tung Sahur")
    description = dc_form_fields_textarea(label="Description", help_text="Information about the contact", placeholder="Is a cool guy", required=False)

class ContactInformationCreateForm(forms.ModelForm):
    class Meta:
        model = ContactInformation
        fields = ["information_type", "content"]
    
    information_type = dc_form_fields_select2_choice(label="Information Type", choices=ContactInformation.INFORMATION_TYPES.choices)
    content = dc_form_fields_textarea(label="Information")
