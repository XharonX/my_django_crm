from productions.models import Product
from .models import Servicing, ErrorReturn


from datetime import datetime
from django import forms


def get_product_selections():
    choices = [['', 'Select the product code']]
    for p in Product.objects.all():
        choices.append((p, p))
    print(choices)
    return choices


class ServiceForm(forms.ModelForm):

    customer = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'customer name',
        'autocomplete': 'off',
        'id': 'customerName'
    }))

    purchase_date = forms.DateTimeField(required=True, widget=forms.SelectDateWidget(
        years=reversed([y for y in range(datetime.now().year-3, datetime.now().year+1)]),
        attrs={
            'class': 'form-control',
            'id': 'purchaseDate',
            'autocomplete': 'off',
        }))

    purchase_shop = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'eg. Junction City',
        'id': 'purchaseShop',

    }))

    product = forms.ModelChoiceField(queryset=Product.objects.all(), empty_label='Select the product code', widget=forms.Select(attrs={
        'class': 'form-control',
        'id': 'productCode',

    }))
    qty = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control offset-md-5',
        'placeholder': 'eg. 1',
        'id': 'productCode',
        'min': 1,
        'style': ' width: 100px',
    }))

    accessories = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'eg. item only or all accessories',
        'id': 'accessories',
    }))

    physical_dmg = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'eg. ကလောတံဖြင့် ထိုးထား၊ ပြင်းထန်ပြုတ်ကျ',
        'id': 'phy-dmg',
    }))

    reason = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'eg. battery ဖောင်းသွားပါသဖြင့်',
        'id': 'reason',
        'style': 'height: 6rem;'
    }))

    class Meta:
        model = ErrorReturn
        fields = '__all__'


class TechFindingForm(forms.ModelForm):
    technician_finding = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'eg. battery ဖောင်းနေပါသည်။ error မှန်ကန်ပါသည်။',
        'id': 'techFinding',
        'style': 'height: 6rem;'
    }))

    final_result = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'eg. reset ချ၍ အဆင်ပြေသေးသည်။',
        'id': 'finalResult',
    }))

    fees = forms.FloatField(widget=forms.NumberInput(attrs={
        'min': '0',
        'class': 'form-control',
        'id': 'serviceFees',
        'style': 'width: 150px;'

    }))

    fees_by = forms.ChoiceField(label='Checked_by',
                                initial='comp',
                                choices=[('cust', 'customer'), ('comp', 'company')],
                                widget=forms.RadioSelect(attrs={
                                        'class': 'form-check-input',
                                    }))

    class Meta:
        model = Servicing
        fields = ['technician_finding', 'final_result', 'fees',]
