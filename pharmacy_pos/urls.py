"""
URL configuration for pharmacy_pos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from django.conf import settings
from supplier.views import supplier_list


def dashboard(request):
    return render(request, 'dashboard.html')


urlpatterns = [
    path("admin/", admin.site.urls),
    path('dashboard', dashboard, name='home'),
    path('suppliers', supplier_list, name='supplier-list')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
