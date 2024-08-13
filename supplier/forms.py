from django import forms


class SupplierForm(forms.Form):
    is_manufectural = forms.BooleanField(required=False)
    supplier_name = forms.CharField()
    supplier_phone = forms.CharField()
