from django.shortcuts import render,  get_object_or_404
from home.models import Product, Category


def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)


def products_list(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,  
        'products': products 
    }
    return render(request, 'products_list.html', context=context)
