from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

# 1. Dashboard Landing Route (Home Page)
def home(request):
    total_products = Product.objects.count()
    # Identifies critical metrics for stock items less than 5 items
    low_stock = Product.objects.filter(quantity__lt=5).count()
    
    context = {
        'total_products': total_products,
        'low_stock': low_stock
    }
    return render(request, 'inventory/home.html', context)


# 2. View Product List & Search Functionality
def product_list(request):
    query = request.GET.get('q', '') # Captures text from the search field
    if query:
        # Performs a search across names or categories matching the string
        products = Product.objects.filter(name__icontains=query) | Product.objects.filter(category__icontains=query)
    else:
        products = Product.objects.all()
        
    return render(request, 'inventory/view_list.html', {'products': products, 'query': query})


# 3. Add Product Page
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})


# 4. Edit Product / Update Stock Page
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory/edit_product.html', {'form': form, 'product': product})


# 5. Delete Product Confirmation
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'inventory/delete_confirm.html', {'product': product})