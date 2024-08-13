from django.shortcuts import render, redirect
from supplier.models import Supplier
from .forms import SupplierForm



def supplier_list(request):
    form = SupplierForm()
    context = {
        "suppliers": Supplier.objects.all(),
        "supplier_form": form
    }

    return render(request, 'supplier/supplier_list.html', context)


def create_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            manufectural = form.cleaned_data['is_manufectural']
            name = form.cleaned_data['supplier_name']
            phone = form.cleaned_data['supplier_phone']

            Supplier.objects.create(
                is_manufactural=manufectural,
                supplier_name=name,
                supplier_phone=phone
            )
            return redirect('supplier-list')

    form = SupplierForm()
    context = {
        "supplier_form": form
    }

    return render(request, 'supplier/create_supplier.html', context)