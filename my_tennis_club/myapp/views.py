from django.shortcuts import render, redirect
from .models import CarBrand
from .forms import CarBrandForm
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

def home(request):
    return render(request, 'home.html')

def brand_list(request):
    if request.method == 'POST':
        form = CarBrandForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            form.save()
            return redirect('brand_list')  # Ensure 'brand_list' is the correct URL name
    else:
        form = CarBrandForm()
    brands = CarBrand.objects.all()
    return render(request, 'myapp/brand_list.html', {'brands': brands, 'form': form})

class CarBrandDeleteView(DeleteView):
    model = CarBrand
    template_name = 'myapp/brand_confirm_delete.html'
    success_url = reverse_lazy('brand_list')

# views.py

from django.shortcuts import render
from .models import CarBrand

def brand_gallery(request):
    brands = CarBrand.objects.all()
    return render(request, 'myapp/brand_gallery.html', {'brands': brands})




