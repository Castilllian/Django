from django.shortcuts import render
from django.http import JsonResponse
from .models import Client, Product, Order

def create_client(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        new_client = Client.objects.create(name=name, email=email, phone_number=phone_number, address=address)
        return JsonResponse({'message': 'Client created successfully'})

def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        new_product = Product.objects.create(name=name, description=description, price=price, quantity=quantity)
        return JsonResponse({'message': 'Product created successfully'})

def create_order(request):
    if request.method == 'POST':
        client_id = request.POST.get('client_id')
        product_ids = request.POST.getlist('product_ids')
        total_amount = request.POST.get('total_amount')
        client = Client.objects.get(pk=client_id)
        products = Product.objects.filter(pk__in=product_ids)
        new_order = Order.objects.create(client=client, total_amount=total_amount)
        new_order.products.set(products)
        return JsonResponse({'message': 'Order created successfully'})