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
            form.save()
            return redirect('supplier-list')

    form = SupplierForm()
    context = {
        "supplier_form": form
    }

    return render(request, 'supplier/create_supplier.html', context)


def delete_supplier(request, supplier_id):
    Supplier.objects.get(id=supplier_id).delete()
    # delete
    return redirect('supplier-list')
