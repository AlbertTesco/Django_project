from django import forms

from catalog.models import Product
from catalog.validators import validate_prohibited_words


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=123)
    message = forms.CharField(widget=forms.Textarea)


class ProductForm(forms.ModelForm):
    name = forms.CharField(validators=[validate_prohibited_words],
                           label="Название",
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'my-input-class',
                                   'required': True
                               }
                           ))
    description = forms.CharField(validators=[validate_prohibited_words],
                                  label="Описание",
                                  widget=forms.Textarea(
                                      attrs={'class': 'my-textarea-class',
                                             'required': True
                                             }
                                  ))

    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'purchase_price']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'my-file-input-class', 'required': False}),
            'category': forms.Select(attrs={'class': 'my-select-class', 'required': True}),
            'purchase_price': forms.NumberInput(attrs={'class': 'my-number-input-class', 'required': True})
        }
