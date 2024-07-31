from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.


def mainContext():
    # Address ve SocialMedia verilerini al
    address = Address.objects.first()
    social_media_links = SocialMedia.objects.all()
    
    # Template'e veri geçirme
    context = {
        'address': address,
        'social_media_links': social_media_links,
    }
    return context




def home(request):
    categories = Category.objects.all() 

    context_data = mainContext()

    context = {
        "categories":categories,
    }

    context_data.update(context)

    return render(request, 'core/home.html', context_data)




def category_detail(request, category_id):
    context_data = mainContext()
    category = get_object_or_404(Category, id=category_id)
    
    products = Product.objects.filter(category=category, available=True)
    
    context = {
        'category': category,
        'products': products,
    }
    
    context.update(context_data)
    return render(request, 'core/category_detail.html', context)