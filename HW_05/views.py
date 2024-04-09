from django.shortcuts import render
from django.http import JsonResponse
from .models import Client, Product, Order
from django.db.models import Prefetch
from datetime import datetime, timedelta
from .forms import ProductPhotoForm

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
        form = ProductPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            photo = form.cleaned_data['photo']
            
            new_product = Product.objects.create(name=name, description=description, price=price, quantity=quantity, photo=photo)
            return JsonResponse({'message': 'Product created successfully'})
    else:
        form = ProductPhotoForm()

    return render(request, 'create_product.html', {'form': form})

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
    
def order_list(request, client_id):
    client = Client.objects.get(pk=client_id)

    # Запрос для получения списка заказанных товаров клиента за последние 7 дней
    date_7_days_ago = datetime.now() - timedelta(days=7)
    orders_last_7_days = Order.objects.filter(client=client, order_date__gte=date_7_days_ago)

    # Запрос для получения списка заказанных товаров клиента за последние 30 дней
    date_30_days_ago = datetime.now() - timedelta(days=30)
    orders_last_30_days = Order.objects.filter(client=client, order_date__gte=date_30_days_ago)

    # Запрос для получения списка заказанных товаров клиента за последние 365 дней
    date_365_days_ago = datetime.now() - timedelta(days=365)
    orders_last_365_days = Order.objects.filter(client=client, order_date__gte=date_365_days_ago)

    context = {
        'client': client,
        'orders_last_7_days': orders_last_7_days,
        'orders_last_30_days': orders_last_30_days,
        'orders_last_365_days': orders_last_365_days,
    }

    return render(request, 'order_list.html', context)