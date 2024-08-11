from django.db import models


class Supplier(models.Model):
    is_manufactural = models.BooleanField()
    supplier_name = models.CharField(max_length=50)
    supplier_phone = models.CharField(max_length=50)



