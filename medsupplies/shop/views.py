from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def staff(request):
    return render(request, 'staff.html')

def equipments(request):
    return render(request, 'equipments.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
import os
from django.conf import settings
from django.shortcuts import render

def equipments(request):
    equipment_images = [f'images/equipment{i}.jpg' for i in range(1, 17)]
    return render(request, 'shop/equipments.html', {'equipment_images': equipment_images})


    # Loop through static images named equipment1.jpg ... equipment16.jpg
    for i in range(1, 17):
        filename = f'equipment{i}.jpg'
        if os.path.exists(os.path.join(images_path, filename)):
            images.append(f'images/{filename}')

    context = {
        'images': images
    }
    return render(request, 'shop/equipments.html')
