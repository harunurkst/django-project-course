from django.shortcuts import render
from supplier.models import Supplier


def supplier_list(request):

    context = {
        "suppliers": Supplier.objects.all()
    }

    return render(request, 'supplier/supplier_list.html', context)