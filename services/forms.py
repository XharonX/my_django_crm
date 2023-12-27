from productions.models import Product
from .models import Servicing, ErrorReturn


from datetime import datetime
from django import forms


def get_product_selections():
    choices = [['', 'Select the product code']]
    for p in Product.objects.all():
        choices.append((p, p))
    return choices


def get_reversed_years(start, end):
    y = []
    for year in range(end, start, -1):
        y.append(year)
    return y


class ServiceForm(forms.ModelForm):

    customer = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-sm rounded-4',
        'placeholder': 'customer name',
        'autocomplete': 'off',
        'id': 'customerName'
    }))

    purchase_date = forms.DateTimeField(required=True, widget=forms.SelectDateWidget(
        years=get_reversed_years(datetime.now().year - 3, datetime.now().year),
        attrs={
            'class': 'form-control rounded-3',
            'id': 'purchaseDate',
            'autocomplete': 'off',
        }))

    purchase_shop = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control rounded-4',
        'placeholder': 'eg. Junction City',
        'id': 'purchaseShop',

    }))

    product = forms.ModelChoiceField(queryset=Product.objects.all(), empty_label='Select the product code', widget=forms.Select(attrs={
        'class': 'form-control rounded-4 ',
        'id': 'productCode',
        'style': 'width: 15rem',

    }))

    # online_sale= forms.CharField(max_length=15, widget=forms.TextInput(attrs={
    #     'class': 'form-control rounded-4',
    #     'id': 'onlinesale_id',
    # }))

    qty = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control rounded-pill offset-md-4',
        'placeholder': 'eg. 1',
        'id': 'productCode',
        'min': 1,
        'style': ' width: 100px',
    }))

    accessories = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control rounded-4 me-4 py-2 px-3',
        'placeholder': 'eg. item only or all accessories',
        'id': 'accessories',
    }))

    physical_dmg = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control rounded-4 py-2 me-5',
        'placeholder': 'eg. ကလောတံဖြင့် ထိုးထား၊ ပြင်းထန်ပြုတ်ကျ',
        'id': 'phy-dmg',
    }))

    reason = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'form-control rounded-4',
        'placeholder': 'eg. battery ဖောင်းသွားပါသဖြင့်',
        'id': 'reason',
        'style': 'height: 6rem;'
    }))
    how_happen = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'form-control rounded-4',
        'placeholder': 'customer သို့မေးမြန်းရန်။ eg.သုံးနေရင်းအလိုလို ရပ်သွားတာ',
        'id': 'happened',
        'style': 'height: 6rem;'
    }))

    class Meta:
        model = ErrorReturn
        fields = '__all__'
        exclude = ['received_by',]


class TechFindingForm(forms.ModelForm):

    technician_finding = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'eg. battery ဖောင်းနေပါသည်။ error မှန်ကန်ပါသည်။',
        'id': 'techFinding',
        'style': 'height: 6rem;'
    }))

    final_result = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'eg. အသစ်အလဲပေးသည်။',
        'id': 'finalResult',
    }))

    fees = forms.FloatField(widget=forms.NumberInput(attrs={
        'min': '0',
        'class': 'form-control',
        'id': 'serviceFees',
        'style': 'width: 150px;'

    }))

    fees_by = forms.ChoiceField(initial='comp',
                                choices=[('cust', 'customer'), ('comp', 'company')],
                                widget=forms.RadioSelect(attrs={
                                        'class': 'form-check-input',
                                    }))

    class Meta:
        model = Servicing
        fields = '__all__'
        exclude = ['form', 'technician']
