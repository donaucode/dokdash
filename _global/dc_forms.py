from django import forms
from django_select2.forms import Select2Widget, Select2MultipleWidget

def dc_form_fields_char(label, help_text="", placeholder="", required=True, **kwargs):
    """Factory for a standard CharField with a TextInput widget."""
    attrs = {"class": "field"}
    if placeholder:
        attrs["placeholder"] = placeholder
        
    return forms.CharField(
        label=label,
        help_text=help_text,
        required=required,
        widget=forms.TextInput(attrs=attrs),
        **kwargs
    )

def dc_form_fields_textarea(label, help_text="", placeholder="", required=True, rows=6, **kwargs):
    """Factory for a CharField that renders as a <textarea>."""
    attrs = {"class": "field", "rows": rows}
    if placeholder:
        attrs["placeholder"] = placeholder
        
    return forms.CharField(
        label=label,
        help_text=help_text,
        required=required,
        widget=forms.Textarea(attrs=attrs),
        **kwargs
    )

def dc_form_fields_choice(label, choices, help_text="", required=True, **kwargs):
    """Factory for a ChoiceField that renders as a <select> dropdown."""
    return forms.ChoiceField(
        label=label,
        help_text=help_text,
        choices=choices,
        required=required,
        widget=forms.Select(attrs={"class": "field"}),
        **kwargs
    )
    
def dc_form_fields_model_choice(label, queryset, help_text="", required=True, empty_label="---------", **kwargs):
    """Factory for a ModelChoiceField that populates a <select> from a queryset."""
    return forms.ModelChoiceField(
        label=label,
        help_text=help_text,
        queryset=queryset,
        required=required,
        empty_label=empty_label,
        widget=forms.Select(attrs={"class": "field"}),
        **kwargs
    )

def dc_form_fields_integer(label, help_text="", placeholder="", required=True, min_value=None, max_value=None, **kwargs):
    """Factory for an IntegerField that renders as an <input type="number">."""
    attrs = {"class": "field"}
    if placeholder:
        attrs["placeholder"] = placeholder

    return forms.IntegerField(
        label=label,
        help_text=help_text,
        required=required,
        min_value=min_value,
        max_value=max_value,
        widget=forms.NumberInput(attrs=attrs),
        **kwargs
    )

def dc_form_fields_decimal(label, help_text="", placeholder="", required=True, max_digits=10, decimal_places=2, **kwargs):
    """
    Factory for a DecimalField, ideal for currency and precise measurements.
    Defaults to 10 total digits and 2 decimal places (e.g., 12345678.99).
    """
    attrs = {"class": "field"}
    if placeholder:
        attrs["placeholder"] = placeholder

    return forms.DecimalField(
        label=label,
        help_text=help_text,
        required=required,
        max_digits=max_digits,
        decimal_places=decimal_places,
        # The widget is still NumberInput, but validation is handled by the field
        widget=forms.NumberInput(attrs=attrs),
        **kwargs
    )

def dc_form_fields_email(label, help_text="", placeholder="", required=True, **kwargs):
    """Factory for an EmailField that renders as an <input type="email">."""
    attrs = {"class": "field"}
    if placeholder:
        attrs["placeholder"] = placeholder

    return forms.EmailField(
        label=label,
        help_text=help_text,
        required=required,
        widget=forms.EmailInput(attrs=attrs),
        **kwargs
    )

def dc_form_fields_boolean(label, help_text="", required=False, **kwargs):
    """
    Factory for a BooleanField that renders as a checkbox.
    Defaults to required=False, which is standard for a single checkbox.
    """
    return forms.BooleanField(
        label=label,
        help_text=help_text,
        required=required,
        widget=forms.CheckboxInput(),
        **kwargs
    )

def dc_form_fields_date(label, help_text="", placeholder="", required=True, **kwargs):
    """Factory for a DateField that uses the browser's date picker."""
    attrs = {"class": "field", "type": "date"}
    if placeholder:
        attrs["placeholder"] = placeholder
        
    return forms.DateField(
        label=label,
        help_text=help_text,
        required=required,
        # This format ensures Django understands the data from <input type="date">
        widget=forms.DateInput(attrs=attrs, format='%Y-%m-%d'),
        **kwargs
    )

def dc_form_fields_select2_model_choice(label, queryset, help_text="", required=True, empty_label="---------", **kwargs):
    """
    Factory for a ModelChoiceField that uses a Select2 widget for a better UI.
    For selecting a SINGLE item from a queryset (e.g., a Foreign Key).
    """
    return forms.ModelChoiceField(
        label=label,
        help_text=help_text,
        queryset=queryset,
        required=required,
        empty_label=empty_label,
        widget=Select2Widget(),
        **kwargs
    )

def dc_form_fields_select2_model_choice_multiple(label, queryset, help_text="", required=True, **kwargs):
    """
    Factory for a ModelMultipleChoiceField that uses a Select2Multiple widget.
    For selecting MULTIPLE items from a queryset (e.g., a ManyToManyField).
    """
    return forms.ModelMultipleChoiceField(
        label=label,
        help_text=help_text,
        queryset=queryset,
        required=required,
        widget=Select2MultipleWidget(attrs={"class": "field"}),
        **kwargs
    )
    
def dc_form_fields_select2_choice_multiple(label, choices, help_text="", required=True, **kwargs):
    """
    Factory for a MultipleChoiceField that uses a Select2Multiple widget.
    For selecting MULTIPLE items from a tuple of choices.
    """
    return forms.MultipleChoiceField(
        label=label,
        help_text=help_text,
        choices=choices,
        required=required,
        widget=Select2MultipleWidget(attrs={"class": "select2-field"}),
        **kwargs
    )
    
def dc_form_fields_file(label, help_text="", required=True, **kwargs):
    """
    Factory for a FileField that renders as an <input type="file">.
    IMPORTANT: The HTML <form> tag must have enctype="multipart/form-data".
    """
    return forms.FileField(
        label=label,
        help_text=help_text,
        required=required,
        widget=forms.FileInput(attrs={"class": "field"}),
        **kwargs
    )

def dc_form_fields_image(label, help_text="", required=True, **kwargs):
    """
    Factory for an ImageField that validates the uploaded file is an image.
    Requires the 'Pillow' library: pip install Pillow
    IMPORTANT: The HTML <form> tag must have enctype="multipart/form-data".
    """
    return forms.ImageField(
        label=label,
        help_text=help_text,
        required=required,
        widget=forms.FileInput(attrs={"class": "field"}),
        **kwargs
    )
